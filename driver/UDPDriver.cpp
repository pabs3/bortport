//
// Created by Shayne O'Neill on 15/4/19.
//

#include "UDPDriver.h"
std::string make_daytime_string()
{
    using namespace std; // For time_t, time and ctime;
    time_t now = time(0);
    return ctime(&now);
}

void error(char const *msg)
{
    perror(msg);
    exit(1);
}

UDPDriver::UDPDriver(boost::asio::io_context& io_context) : socket_(io_context, udp::endpoint(udp::v4(), 6901))
{
    start_receive();
}

void UDPDriver::start_receive()
{
    socket_.async_receive_from(
            boost::asio::buffer(recv_buffer_), remote_endpoint_,
            boost::bind(&UDPDriver::handle_receive, this,
                        boost::asio::placeholders::error,
                        boost::asio::placeholders::bytes_transferred));
}

void UDPDriver::handle_receive(const boost::system::error_code& error,
                    std::size_t size /*bytes_transferred*/)
{
    if (!error)
    {
        //udp::endpoint* remote_endpoint_ = new udp::endpoint(); // endpoint object is cleaned up by handler
        //socket_.receive_from( // Go ahead and make everything synchronous for testing purposes--------------------
        //        boost::asio::buffer(recv_buffer_), *remote_endpoint_); // Should stay as a synchronous call to maintain a listening thread.
        std::cout << "receive_from() called" << size << std::endl;

        MidiMessage message;
        size_t len = socket_.receive_from((recv_buffer_), remote_endpoint_);
        std::cout.write(recv_buffer_.data(),len);
        //std::istream* inStream = new std::istream(recv_buffer_);
        message.ParseFromArray(recv_buffer_.data(),len);
        std::cout << message.message_id() << "BORT" << std::endl;



        /*
         socket_.async_send_to(boost::asio::buffer(*message), remote_endpoint_,
                               boost::bind(&UDPDriver::handle_send, this, message,
                                           boost::asio::placeholders::error,
                                           boost::asio::placeholders::bytes_transferred));
         */
        start_receive();
    } else {
        std::cout << "Woops\n";
    }
}

void UDPDriver::handle_send(boost::shared_ptr<std::string> /*message*/,
                 const boost::system::error_code& /*error*/,
                 std::size_t /*bytes_transferred*/)
{
}