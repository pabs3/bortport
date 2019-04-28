//
// Created by Shayne O'Neill on 24/4/19.
//

#ifndef DRIVER_ENGINE_H
#define DRIVER_ENGINE_H

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



class Engine  : public QObject {
    Q_OBJECT

public:
    explicit Engine(QObject *parent = 0);

    void processMessage(MidiMessage *message);
    void raiseError (Error_ErrorSeverity severity, std::string description);

signals:
    int messageSend(MidiData data);
public slots:
    int messageRecieve(MidiMessage* message);
private:


};


#endif //DRIVER_ENGINE_H
