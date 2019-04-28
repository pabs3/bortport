cmake_minimum_required(VERSION 3.12)
project(driver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
add_compile_definitions(__RTMIDI_DEBUG__ )

add_compile_definitions(__MACOSX_CORE__)
add_compile_definitions(PLATFORM_OSX)


    find_library( coreaudio_lib CoreAudio )
    find_library( coremidi_lib CoreMIDI )
    find_library( corefoundation_lib CoreFoundation )
    find_library( audiotoolbox_lib AudioToolbox )
    find_library( audiounit_lib AudioUnit )

    set( _midi_libs
            ${coreaudio_lib}
            ${coremidi_lib}
            ${corefoundation_lib}
            ${audiotoolbox_lib}
            ${audiounit_lib}
            )
    set( _midi_defs __MACOSX_AU__ __MACOSX_CORE__ )




find_package(Boost REQUIRED system)

set(CMAKE_PREFIX_PATH "/Users/shayneoneill/Qt/5.12.1/clang_64/lib/cmake")
#set(RT_PREFIX_PATH "/usr/local/Cellar/rtmidi/3.0.0")
find_package(Qt5Core REQUIRED)
find_package(Qt5Network REQUIRED)

add_compile_definitions(__RTMIDI_DEBUG__ )

add_compile_definitions(__MACOSX_CORE__)

find_package(Protobuf REQUIRED)
PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS ${PROJECT_SOURCE_DIR}/../protobuf/src/midimessage.proto)

include_directories('.')
include_directories('/Users/shayneoneill/Qt/5.12.1/clang_64/include')
#include_directories('${RT_PREFIX_PATH}/include')



add_executable(driver main.cpp ${PROTO_SRCS} ${PROTO_HDRS} UDPDriver.cpp UDPDriver.h MidiDriver.cpp MidiDriver.h Engine.cpp Engine.h RtMidi.cpp RtMidi.h)

target_link_libraries(driver ${Protobuf_LIBRARIES})
target_link_libraries(driver Qt5::Core)
target_link_libraries(driver Qt5::Network)
target_link_libraries(driver ${_midi_libs} )

#target_link_libraries(driver ${RT_PREFIX_PATH}/lib/librtmidi.dylib)

