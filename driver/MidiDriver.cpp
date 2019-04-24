//
// Created by Shayne O'Neill on 24/4/19.
//

#include "MidiDriver.h"




MidiDriver::MidiDriver(QObject *parent) :  QObject(parent) {


}

int MidiDriver::add_midi(const std::string& name) {

    RtMidiIn *inPort = 0;
    RtMidiOut *outPort = 0;
    MidiDevice mdev;
    try {
        inPort = new RtMidiIn();
        inPort->openVirtualPort(name);
        outPort = new RtMidiOut();
        outPort->openVirtualPort(name);
    }
    catch ( RtMidiError &error ) {
        error.printMessage();
        return -1;
        //exit( EXIT_FAILURE );
    }
    mdev.inPort = inPort;
    mdev.outPort = outPort;
    mdev.name = name;
    midi_devices.insert(QString::fromStdString(name),mdev);


    return 1;
}

void MidiDriver::setEngine(Engine *engine) {
    MidiDriver::engine = engine;
}

