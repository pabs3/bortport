//
// Created by Shayne O'Neill on 15/4/19.
//

#include "UDPDriver.h"
#include "Engine.h"

UDPDriver::UDPDriver(QObject *parent) :
        QObject(parent)
{

    socket = new QUdpSocket(this);

    socket->bind(QHostAddress::LocalHost, 6901);

    connect(socket, SIGNAL(readyRead()), this, SLOT(readyRead()));
    std::cout << "Reading\n";
    setAddress(QHostAddress::LocalHost);
    setPort(6902);
    //address = QHostAddress::LocalHost;
    //port = 6902;
}


int UDPDriver::messageSend(MidiMessage* message) {
    QByteArray data;
    std::string serialized = message->SerializeAsString();
    data.append(serialized.c_str(),serialized.length());
    socket->writeDatagram(data,address,port);
    return 1;
}

void UDPDriver::readyRead()
{
    // when data comes in
    QByteArray buffer;
    buffer.resize(socket->pendingDatagramSize());

    QHostAddress sender;
    quint16 senderPort;

    socket->readDatagram(buffer.data(), buffer.size(),
                         &sender, &senderPort);

    qDebug() << "Message from: " << sender.toString();
    qDebug() << "Message port: " << senderPort;
    qDebug() << "Message: " << buffer;
    MidiMessage msg;
    msg.ParseFromString(buffer.toStdString());
    std::cout << msg.DebugString();
    engine->processMessage(&msg);
}

void UDPDriver::setEngine(Engine *engine) {
    UDPDriver::engine = engine;
}

const QHostAddress &UDPDriver::getAddress() const {
    return address;
}

void UDPDriver::setAddress(const QHostAddress &address) {
    UDPDriver::address = address;
}

int UDPDriver::getPort() const {
    return port;
}

void UDPDriver::setPort(int port) {
    UDPDriver::port = port;
}
