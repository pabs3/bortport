//
// Created by Shayne O'Neill on 24/4/19.
//

#include "MidiDriver.h"




MidiDriver::MidiDriver(QObject *parent) :  QObject(parent) {
}

struct DriverPointer {
    MidiDriver* md = 0;
    int chan = 0;
};


void static_callback(double deltatime, std::vector< unsigned char > *message, void *userData ) {
    //std::cout << message << "\n";
    DriverPointer *driver = static_cast<DriverPointer *>(userData);
    driver->md->callback(driver->chan,deltatime,message,userData);
}


int MidiDriver::add_midi(const std::string& name,
                         PortDescription_Direction direction,
                         bool dynamic,
                         int key) {

    RtMidiIn *inPort = 0;
    RtMidiOut *outPort = 0;
    MidiDevice mdev;
    using namespace std::placeholders;  // for _1, _2, _3...
    if (midi_devices.contains(key)) {
        std::cout << "Channel already allocated\n";
        return 1;
    }
    mutex.lock();
    try {
        switch (direction) {
            case PortDescription_Direction_IN: {
                inPort = new RtMidiIn();
                inPort->openVirtualPort(name);
                DriverPointer* db = new DriverPointer;
                db->md = this;
                db->chan = key;
                inPort->setCallback(static_callback, db);
                break;
            }
            case PortDescription_Direction_OUT: {
                outPort = new RtMidiOut();
                outPort->openVirtualPort(name);
                break;
            }
            case PortDescription_Direction_INOUT: {
                inPort = new RtMidiIn();
                inPort->openVirtualPort(name);
                outPort = new RtMidiOut();
                outPort->openVirtualPort(name);
                DriverPointer* db = new DriverPointer;
                db->md = this;
                db->chan = key;
                inPort->setCallback(static_callback, db);
                break;
            }
            default:
                break;
        }
    }
    catch ( RtMidiError &error ) {
        error.printMessage();
        return -1;
        //exit( EXIT_FAILURE );
    }
    mutex.unlock();
    mdev.inPort = inPort;
    mdev.outPort = outPort;
    mdev.name = name;
    midi_devices.insert(key,mdev);

    std::cout << "Created Port " << name << " for key " << key << "\n";
    return 1;
}

void MidiDriver::callback(int chan,  double deltatime, std::vector< unsigned char > *message, void *userData )
{
    unsigned int nBytes = message->size();
    MidiMessage* midiMessage = new MidiMessage;
    midiMessage->set_message_type(MidiMessage_MessageTypes_MIDI_DATA);
    MidiData* midiData = new MidiData;
    midiData->set_channel(chan);
    std::string data(message->begin(),message->end());
    midiData->set_data(data);
    midiMessage->set_allocated_midi_data(midiData);
    engine->messageRecieve(midiMessage);

}



int MidiDriver::sendMessage(MidiData data) {
    //std::cout << "Sending data" << data.DebugString() << "\n";
    int channel = data.channel();
    if (!midi_devices.contains(channel)) {
        std::cout << "Refusing. No Midi channel allocated" << "\n";
        return -1;
    }
    std::string dat = data.data();
    std::vector<unsigned char>* midi = new std::vector<unsigned char>(dat.begin(), dat.end());
    MidiDevice dev = midi_devices[channel];

    mutex.lock();
    try {
        //RtMidiOut mout = *(dev.outPort);
        dev.outPort->sendMessage(midi);
        mutex.unlock();

        return 1;
    } catch ( RtMidiError &error ) {
        error.printMessage();
        mutex.unlock();

        return -1;
        //exit( EXIT_FAILURE );
    }
}

void MidiDriver::setEngine(Engine *engine) {
    MidiDriver::engine = engine;
}

