# VU_ComputerNetworks

This repository includes the assignments for Computer Networks at VU University the year 2017-2018


# Framing:

We use the Ada Lovelace Protocol (ALP). This protocol uses frames with a layout similar to Ethernet frames. An ALP frame contains: 2 bytes for destination, 2 bytes for source, 4 bytes for the length of the frame, 0-64 bytes for the payload, and 1 byte for the checksum.
To calculate the value of checksum bits, ALP uses the following algorithm: add up all the bytes in the frame (excluding the checksum bytes), and take the result modulo (decimal) 128.
We implement a simplified version of the process that handles incoming bits from the physical layer. The task of this process is to distinguish individual frames from a stream of bits. It also checks the intended recipient of frame and if any errors occurred during transmission. Your program receives its input via stdin and must output via stdout.
In reality, the payload of the data-frame would not simply be ASCII-encoded text. Rather, it would contain the headers and trailers added to the actual payload by the higher layers in the networking stack.


# Backwards Learning

We implement a backwards-learning algorithm to be used in network switches. These switches use ALPv2. The protocol is identical to ALP, except for two important details:
1. The length field is now only 2 bytes large.
2. The checksum is only computer over the payload. The source, destination, and length fields are not included in the checksum calculation.
The switch receives frames on multiple links. Our code needs to forward these frames on the appropriate links. You may assume that machines never change the link to which they are connected. You may also assume that you are always allowed to transmit on a link, even if multiple machines are connected to it; you can ignore potential collisions. Frames are forwarded to their destination, even if their CRC checksum indicates a transmission error.

The output should have the following format:
1. m lines, each with the original frame, followed by all ports on which the frame is sent out by your switch. All values are space separated. If the frame is not sent out on any links, the line only contains the original frame.
Initially, it is unknown how the machines are connected to the different ports. In the backward-learning algorithm, when the location of a machine is unknown, the message is flooded. If a message is sent out on multiple links, these links should appear in ascending order in the output.


# Routing

We will implement a “router” process that takes as input a routing table and some destination IPs, and outputs for each destination IP the appropriate forwarding gateway. Your program will receive its input via stdin, and must output via stdout.
We must output the appropriate gateway for each destination IP address, according to the table and the routing principles.


# Distance Vector Routing

The next task is to implement the distance vector routing algorithm. Starting with an empty routing table, we build up a routing table over time from the routing packets we receive. There are data packets interleaved with the routing packets, so we cannot build our table first and only then start using it. While building our table, we must output a single line containing one of the following for every packet you receive:

• NO ROUTE if we do not know where to route the packet.
• next delay, where next is the address of the neighboring machine to which the packet should be forwarded,
  and delay is the estimated delay to the final destination of the packet, as decimal number.
• THANK YOU if the packet is a routing packet for your router.




I also attach the sample inputs for each of the assignments.
