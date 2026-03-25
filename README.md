# cs333-network-utils-temp-name

This repository contains a collection of network utilities for educational purposes. 

## Team Members
- Megan Barco
- Lauren Nutting
- Isaac Kim

## Network Packet Structure
### TCP Packet
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

## Parsing a binary packet in `tcp_parser.py`
This parser converts a raw binary TCP segment (a sequence of bytes) into a structured Python object with readable fields like ports, sequence numbers, flags, and payload.

This works by:
1. Reading fixed-size fields from the header
2. Extracting header length
3. Separating the payload
4. Decoding flags into human-readable values
5. String representation

#### Step 1: Unpacking the TCP Header
```python3
struct.unpack('!HHLLBBHHH', self.raw[:20])
```
We read the first 20 bytes of the packet (minimum TCP header size, no options).

Format breakdown:
| Code | Size | Meaning |
| --- | --- | --- | 
| ! | -- | Network byte order (big-endian) |
| H | 2 bytes | Source port | 
| H | 2 bytes | Destination port | 
| L | 4 bytes | Sequence number | 
| L | 4 bytes | Acknowledgement number | 
| B | 1 byte | Data offset + reserved bits | 
| B | 1 byte | Flags | 
| H | 2 bytes | Source port | 
| H | 2 bytes | Source port | 
| H | 2 bytes | Source port | 

So the line of code transforms raw bytes into meaningful values.

### Step 2: Extracting Header Length
```python
self.data_offset = (offset_res >> 4) * 4
```
The `offset_res` byte contains two thigs:
- 4 bits: header length (data offset)
- 4 bits: reserved

**How it works**
1. Shift right 4 bits to isolate the header length:
```python3
offset_res >> 4
```
2. Multiply by 4. TCP stores length in *4-byte words*, not bytes.

### Step 3: Extracting the Payload
```python3
self.payload = self.raw[self.data_offset:]
```
Now that we know where the header ends, everything after that is the payload. 

### Step 4: Decoding Flags
```python3
self.flag_bits = {
    "FIN": bool(self.flags & 0x01),
    "SYN": bool(self.flags & 0x02),
    "RST": bool(self.flags & 0x04),
    "PSH": bool(self.flags & 0x08),
    "ACK": bool(self.flags & 0x10),
    "URG": bool(self.flags & 0x20),
}
```
The flag byte is a set of *bit flags*, where each bit represents a control signal.

### Step 5: String Representation
Shows a readable summary of the packet. 