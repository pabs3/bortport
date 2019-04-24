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
}

void UDPDriver::sendPacket()
{
    QByteArray Data;
    Data.append("Hello from UDP");

    // qint64 QUdpSocket::writeDatagram(const QByteArray & datagram, 
    //                      const QHostAddress & host, quint16 port)
    socket->writeDatagram(Data, QHostAddress::LocalHost, 1234);
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
