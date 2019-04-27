cmake_minimum_required(VERSION 3.12)
project(driver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
add_compile_definitions(__RTMIDI_DEBUG__ )


    set( _midi_libs )
    set( _midi_defs )




find_package(Boost REQUIRED system)

find_package(Qt5Core REQUIRED)
find_package(Qt5Network REQUIRED)

add_compile_definitions(__RTMIDI_DEBUG__ )

find_package(Protobuf REQUIRED)
PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS ${PROJECT_SOURCE_DIR}/../protobuf/src/midimessage.proto)

include_directories('.')
#include_directories('${RT_PREFIX_PATH}/include')



add_executable(driver main.cpp ${PROTO_SRCS} ${PROTO_HDRS} UDPDriver.cpp UDPDriver.h MidiDriver.cpp MidiDriver.h Engine.cpp Engine.h RtMidi.cpp RtMidi.h)

target_link_libraries(driver ${Protobuf_LIBRARIES})
target_link_libraries(driver Qt5::Core)
target_link_libraries(driver Qt5::Network)
target_link_libraries(driver ${_midi_libs} )

#target_link_libraries(driver ${RT_PREFIX_PATH}/lib/librtmidi.dylib)

