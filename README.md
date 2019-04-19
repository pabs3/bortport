# bortport
The BORT Port. A specification and code for sending multiplexed midi and control metadata over UDP

The Python "driver" already works to some extent, although not all the basic commands are in yet.

So far a remote host can declare itself to the device, and request a number of ports be created (or reopened) , and then midi messages will be sent to and from this.

The protocol buffers spec in protobuf/ is the source of truth for the protocol. This defines it at the application layer. There is absolutely nothing to stop the developer creating a TCP version of this, and in fact this might even be more reliable, if less performant

The goal is to eventually reimplement in something like C or Go. Crystal lang would be our first choice, however the windows port of crystallang is still a work in progress, so for now we'll do this the old fashion way.

Feel free to implement your own versions of this, and even contribute it to this repo. And pull requests are welcome.

Enjoy.

Please note: The C++ stuff in 'driver' is faaaar from useable. For now its just me experimenting with some libraries to figure out how they work. C++ is not my native tounge!
