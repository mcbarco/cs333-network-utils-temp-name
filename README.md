# cs333-network-utils-temp-name

This repository contains a collection of network utilities for educational purposes. 

## Team Members
- Megan Barco
- Lauren Nutting
- Isaac Kim

## Network Packet Structure
## TCP Packet
```
 +-------------------------------+-------------------------------+
 |        Source Port            |     Destination Port          |
 +-------------------------------+-------------------------------+
 |                      Sequence Number                          |
 +---------------------------------------------------------------+
 |                   Acknowledgment Number                       |
 +----+------+------------+--------------------------------------+
 |Hdr | Res  |   Flags    |            Window Size               |
 |Len |      |            |                                      |
 +-------------------------------+-------------------------------+
 |        Checksum               |        Urgent Pointer         |
 +-------------------------------+-------------------------------+
 |            Options (if any) + Padding                         |
 +---------------------------------------------------------------+
```
A TCP packet is created at the transport layer to deliver data between
applications. 
