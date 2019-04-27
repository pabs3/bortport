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
#include <QMutexLocker>

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

    QHash<int,MidiDevice> midi_devices;

    int add_midi(const std::string& name,
                 PortDescription_Direction direction,
                 bool dynamic,
                 int key);
    void setEngine(Engine *engine);

    void callback(int chan, double deltatime, std::vector< unsigned char > *message, void *userData );

signals:

public slots:
    int sendMessage(MidiData data);
private:
    Engine* engine = 0;
    QMutex mutex;
};


#endif //DRIVER_MIDIDRIVER_H
