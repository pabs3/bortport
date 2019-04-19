//
// Created by Shayne O'Neill on 15/4/19.
//

#ifndef DRIVER_UDPDRIVER_H

#include "midimessage.pb.h"
#include <ctime>
#include <iostream>
#include <string>
#include <boost/array.hpp>
#include <boost/bind.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/asio.hpp>
#include <google/protobuf/message.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include "midimessage.pb.h"


#define DRIVER_UDPDRIVER_H

using boost::asio::ip::udp;

class UDPDriver {

public:
    UDPDriver(boost::asio::io_context& io_context);
//        : socket_(io_context, udp::endpoint(udp::v4(), 13));

private:
    void start_receive();
    void handle_receive(const boost::system::error_code& error,
                        std::size_t /*bytes_transferred*/);
    void handle_send(boost::shared_ptr<std::string> /*message*/,
                     const boost::system::error_code& /*error*/,
                     std::size_t /*bytes_transferred*/);
    udp::socket socket_;
    udp::endpoint remote_endpoint_;
    boost::array<char, 512> recv_buffer_;
};



#endif //DRIVER_UDPDRIVER_H
