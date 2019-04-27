//
// Created by Shayne O'Neill on 24/4/19.
//

#include "Engine.h"


#import "MidiDriver.h"
#import "UDPDriver.h"

UDPDriver *udpDriver;
MidiDriver *midiDriver;


Engine::Engine(QObject *parent)  : QObject(parent) {
    udpDriver = new UDPDriver;
    midiDriver = new MidiDriver;
    udpDriver->setEngine(this);
    midiDriver->setEngine(this);

    connect (this,&Engine::messageSend,midiDriver,&MidiDriver::sendMessage);


}

void Engine::processMessage(MidiMessage *message) {

    switch (message->message_type()) {
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_PORT_REQUEST: {
            std::cout << "Port Req \n";

            break;
        }
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_HOST_ANNOUNCE: {
            std::cout << "Announce \n";
            MessageMetadata mdat = message->message_metadata();
            std::string addr = mdat.host();
            int port = mdat.port();
            std::string name = mdat.friendly_name();
            QHostAddress *qadr = new QHostAddress(QString::fromStdString(addr));
            udpDriver->setAddress(*qadr);
            udpDriver->setPort(port);
            PortList ports = mdat.ports();
            for (int i = 0; i < ports.ports_size(); ++i) {
                PortDescription pd = ports.ports(i);
                PortDescription_Direction dir = pd.direction();
                std::string name = pd.name();
                bool dynamic = pd.create_dynamic();
                int key = pd.key();
                midiDriver->add_midi(name, dir, dynamic, key);
            }
            break;
        }
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_MIDI_DATA: {
            //std::cout << "Data \n";
            MidiData data = message->midi_data();
            //midiDriver->sendMessage(data);
            emit messageSend(data);
            break;
        }
        default:
            std::cout << "DEFAULT \n";
    }

}

int Engine::messageRecieve(MidiMessage* message) {
    return udpDriver->messageSend(message);
}