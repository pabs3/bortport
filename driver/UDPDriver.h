//
// Created by Shayne O'Neill on 15/4/19.
//


#ifndef DRIVER_UDPDRIVER_H

#define DRIVER_UDPDRIVER_H
#include "midimessage.pb.h"
#include <ctime>
#include <iostream>
#include <string>

#include <google/protobuf/message.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include "midimessage.pb.h"
#include <QObject>
#include <QUdpSocket>

class Engine;

class UDPDriver : public QObject {
    Q_OBJECT

public:
    explicit UDPDriver(QObject *parent = 0);
    void sendPacket();
    void setEngine(Engine *engine);

signals:

public slots:
    void readyRead();

private:
    QUdpSocket *socket;
    Engine     *engine = 0;
    QHostAddress address;
public:
    const QHostAddress &getAddress() const;

    void setAddress(const QHostAddress &address);

    int getPort() const;

    void setPort(int port);

    int messageSend(MidiMessage* message);

private:
    int port;

};



#endif //DRIVER_UDPDRIVER_H
