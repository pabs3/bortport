
from __future__ import print_function

import signal
import pyuv
import mido
import midimessage_pb2 as mm
from functools import partial
import uuid
import sqlite3
import datetime
import uuid


hexify = lambda y:":".join(list(map(lambda x: hex(x),y)))

create_table_sql = """
CREATE TABLE midi 
(session string, direction integer, device int, 
data string, timestamp datetime, desc string, notes text
)
"""

insert_data_sql = """
INSERT INTO midi VALUES (?, ?,?,?,?,?,?)
"""

class Monitoring:

    def __init__(self):
        self.conn = sqlite3.connect('logs.db')
        self.c = self.conn.cursor()
        self.session = "none and weird"

    def setup_tables(self):
        self.c.execute(create_table_sql)

    def write_record(self,direction,device,data,desc):
        data_text = hexify(data)
        date = datetime.datetime.now()
        self.c.execute(insert_data_sql,[self.session,direction,device,data_text,date,desc,''])
        self.conn.commit()

class MidiDriver:
    midi_devs = {}

    stop = False

    signal_h = None
    server   = None
    replyport = 6902
    replyaddr = "127.0.0.1"



    def on_read(self, handle, ip_port, flags, data, error):
        msg = mm.MidiMessage.FromString(data)
        #import ipdb; ipdb.set_trace()
        print(msg)
        if msg.message_type == 0:
            self.host_announced(msg)
        if msg.message_type == 4:
            self.midi_msg(msg)

    def host_announced(self, msg):
        self.monitor.session = uuid.uuid4().__str__()
        replyport = msg.message_metadata.port
        replyaddr = msg.message_metadata.host
        meta = msg.message_metadata
        # Send ack back.
        ports = meta.ports.ports
        print ("Connection from {} on host {} port {}".format(meta.friendly_name,meta.host,meta.port))
        print ("Node type is {} version {} ".format(meta.software_package,meta.software_version))
        for k,v in self.midi_devs.items():
            v.close()
        self.midi_devs = {}
        for port in ports:
            self.open_port(port.key, port.name, port.create_dynamic)

    def midi_msg(self , msg):
        midi = mido.Message.from_bytes(msg.midi_data.data)
        device = msg.midi_data.channel
        self.monitor.write_record(2,device,msg.midi_data.data,midi.__str__())
        print ("On {} Got {}".format(device,midi))
        dev = self.midi_devs[device]
        dev.send(midi)


    def signal_cb(self,handle, signum):
        self.signal_h.close()
        self.server.close()

    def process_midi(self,chan,msg):
        print ("Got midi message on channel {}:{}".format(chan,msg.bytes()))
        #return
        data = msg.bytes()
        message = mm.MidiMessage()
        message.message_id = uuid.uuid4().__str__()
        message.last_message = "none"
        message.message_type = message.MIDI_DATA
        message.midi_data.channel = chan
        message.midi_data.data = bytes(msg.bytes())
        packet = message.SerializeToString()
        self.monitor.write_record(1,chan,data,msg.__str__())
        self.server.send((self.replyaddr,self.replyport),packet)


    def open_port(self,key,port_name,virtual):
        print ("OPENING PORT: {} : {} (Virtual:{})".format(key,port_name,virtual))
        #cb = partial(self.process_midi, key)
        midi_dev = mido.open_ioport(name=port_name, virtual=virtual)
        self.midi_devs[key] = midi_dev


    def main(self,m):
        self.monitor = m
        self.loop = pyuv.Loop.default_loop()

        self.server = pyuv.UDP(self.loop)
        self.server.bind(("0.0.0.0", 6901))
        self.server.start_recv(self.on_read)

        self.signal_h = pyuv.Signal(self.loop)
        self.signal_h.start(self.signal_cb, signal.SIGINT)

        print("PyUV version %s" % pyuv.__version__)
        #self.setup_midi()

        while not self.stop and self.loop.run(pyuv.UV_RUN_NOWAIT):
            for k,v in self.midi_devs.items():
                for msg in v.iter_pending():
                    self.process_midi(k,msg)
        print("Stopped!")

driver = MidiDriver()
m = Monitoring()
try:
    m.setup_tables()
except:
    print  ("Midi logs db already created")
driver.main(m)