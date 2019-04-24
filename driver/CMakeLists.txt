cmake_minimum_required(VERSION 3.12)
project(driver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

find_package(Boost REQUIRED system)

set(CMAKE_PREFIX_PATH "/Users/shayneoneill/Qt/5.12.1/clang_64/lib/cmake")
set(RT_PREFIX_PATH "/usr/local/Cellar/rtmidi/3.0.0")
find_package(Qt5Core REQUIRED)
find_package(Qt5Network REQUIRED)



find_package(Protobuf REQUIRED)

include_directories('.')
include_directories('/Users/shayneoneill/Qt/5.12.1/clang_64/include')
include_directories('${RT_PREFIX_PATH}/include')



add_executable(driver main.cpp midimessage.pb.cc midimessage.pb.h UDPDriver.cpp UDPDriver.h MidiDriver.cpp MidiDriver.h Engine.cpp Engine.h)

target_link_libraries(driver ${Protobuf_LIBRARIES})
target_link_libraries(driver Qt5::Core)
target_link_libraries(driver Qt5::Network)
target_link_libraries(driver ${RT_PREFIX_PATH}/lib/librtmidi.dylib)

