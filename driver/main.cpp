#include <iostream>
#import "UDPDriver.h"
int main() {
    try
    {
        boost::asio::io_context io_context;
        UDPDriver server(io_context);
        io_context.run();
    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
    return 0;
}