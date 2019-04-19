cmake_minimum_required(VERSION 3.12)
project(driver)

set(CMAKE_CXX_STANDARD 17)

find_package(Boost REQUIRED system)

IF (Boost_FOUND)
    include_directories(${Boost_INCLUDE_DIR})
endif()

find_package(Protobuf REQUIRED)


add_executable(driver main.cpp midimessage.pb.cc midimessage.pb.h UDPDriver.cpp UDPDriver.h)

target_link_libraries(driver ${Protobuf_LIBRARIES} ${Boost_LIBRARIES})
