#include <iostream>
#include <QCoreApplication>
#include "Engine.h"
int main(int argc, char *argv[]) {
    try
    {
        std::cout << "Bort Port v0.9 (C) Bort Orbital Research Temple Pty Ltd.\n====[[TO THE MOOOOOOOON]======" << std::endl;

        QCoreApplication a(argc, argv);

        Engine engine;

//        UDPDriver client;
        //
//        client.HelloUDP();     //   ;
        return a.exec();

    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
    return 0;
}