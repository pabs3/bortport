//
// Created by Shayne O'Neill on 24/4/19.
//

#ifndef DRIVER_MIDIDRIVER_H
#define DRIVER_MIDIDRIVER_H

#include "midimessage.pb.h"
#include <ctime>
#include <iostream>
#include <string>

#include <google/protobuf/message.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include "midimessage.pb.h"
#include <QObject>
#include <QHash>
#include "RtMidi.h"

#include "Engine.h"


struct MidiDevice {
    RtMidiIn *inPort = 0;
    RtMidiOut *outPort = 0;
    std::string name = "";
};

class MidiDriver : public QObject
{
    Q_OBJECT
public:
    explicit MidiDriver(QObject *parent = 0);

    QHash<QString,MidiDevice> midi_devices;

    int add_midi(const std::string& name);

signals:

public slots:

private:
    Engine* engine = 0;
public:
    void setEngine(Engine *engine);
};


#endif //DRIVER_MIDIDRIVER_H
