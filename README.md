# Bortport

The BORT Port. A specification and code for sending multiplexed midi and control metadata over UDP

The Python "driver" already works to some extent, although not all the basic commands are in yet.

So far a remote host can declare itself to the device, and request a number of ports be created (or reopened) , and then midi messages will be sent to and from this.

The protocol buffers spec in protobuf/ is the source of truth for the protocol. This defines it at the application layer. There is absolutely nothing to stop the developer creating a TCP version of this, and in fact this might even be more reliable, if less performant

The goal is to eventually reimplement in something like C or Go. Crystal lang would be our first choice, however the windows port of crystallang is still a work in progress, so for now we'll do this the old fashion way.

Feel free to implement your own versions of this, and even contribute it to this repo. And pull requests are welcome.

Enjoy.

# C++ 'Driver'

The C++ Driver is now basically useful. It has a few shortcomings.

1) Windows is incapable of natively supporting Virtual Midi Devices, whereas OSX and GNU/Linux (ALSA/Jack) does. This will require writing a small kernel driver to implement this. Its likely this driver can not be provided under a GPL license, we might have to ask the FSF if the LGPL is compatible. Otherwise we might have to use a more permissive alternative.

2) The build system is currently hard-wired for the primary authors Macbook. We'll fix that eventually. Pull requests are welcome!

3) The driver does not yet support resending lost packets, however provisions exist for it in the protocol.

4) Clear security shortcomings exist. There is no encryption, and no verification of the host announce protocol leading to potential reflection attacks. We'll add in encryption sooner than later, and suggestions for mitigating reflection attacks would be welcomed.

5) Also Unimplemented are Host Retire, Port Request,  (Its folded into Host Announce), and the Pub Sub functions.

6) Midi device unavailable messages might get sent to the wrong address if caused by a lost announcement. This needs some pondering.

7) Eventually installers for the Mac and Windows system, and distribution packaging for the GNU/Linux systems would be needed.

# Protocol basics

The protocol is simple.

The Client device sends the host a "Host announce" packet. The packet should contain the clients address/port and a list of requested virtual midi devices with names and a number to enumerate the device. If the enumerated device exists, an error marked warning should reply that the device exists already. This should not be a show stopper error, just a notification.

The client and server can then send each other MIDI_DATA messages with raw midi data and an index pointing to the enumerated midi devices.

If the enumerated device does not exist the host should respond with an error, which should prompt the client to respond with a host announce or port request.

When the Client finishes it should send a Host Retire. But the Host should be resilient about the fact that the host retirement might not ever be sent, as UDP is connectionless.

# Pub/Sub

This functionality is , as of now, unimplemented and not fully planned. The goal is to allow things like VST plugins and DAWs the ability to form a back channel over the wire to provide richer content streams than MIDI provides for. For instance an EQ plugin could send spectrum plots to be rendered on a control device, or a DAW might provide customised control data that does not fit the Mackie/Logic Pro control protocol.

Its anticipated, but not locked in that this should hook in to DBUS on either side of the link. However nothing is set in stone, and a security evaluation should be undertaken to ascertain whether this functionality could open devices to critical security vunerabilities. DBUS is a very powerful system, and like fire it can burn the uninitiated.
