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


}

void Engine::processMessage(MidiMessage *message) {

    switch (message->message_type()) {
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_PORT_REQUEST:
            std::cout << "Port Req \n";

            break;
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_HOST_ANNOUNCE:
            std::cout << "Announce \n";


            break;
        case MidiMessage_MessageTypes::MidiMessage_MessageTypes_MIDI_DATA:
            std::cout << "Data \n";

            break;
        default:
            std::cout << "DEFAULT \n";
    }


}
