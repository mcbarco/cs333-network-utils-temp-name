import struct

class TCPPacketParser:
    def __init__(self, raw_data: bytes):
        self.raw = raw_data

        # Parse immediately
        self._parse()

    def _parse(self):
        # Unpack first 20 bytes (typical TCP header size without options)
            # NOTE: struct.unpack format:
            # ! - network byte order (big-endian)
            # H - unsigned short (2 bytes)
            # L - unsigned long (4 bytes)
            # B - unsigned char (1 byte)
        (
            self.src_port,  # source port, 2 bytes (H)
            self.dst_port,  # destination port, 2 bytes (H)
            self.seq,       # sequence number, 4 bytes (L)
            self.ack_seq,   # acknowledgment number, 4 bytes (L)
            offset_res,     # data offset (where data begins) and reserved bits, 1 byte (B)
            self.flags,     # flags, 1 byte (B)
            self.window,    # window size, 2 bytes (H)
            self.checksum,  # checksum, 2 bytes (H)
            self.urg_ptr    # urgent pointer, 2 bytes (H)
        ) = struct.unpack("!HHLLBBHHH", self.raw[:20]) 

        # Extract header length
            # offset_rest >> 4 removes the reserved bit
            # * 4 to get to minimum TCP header size
        self.data_offset = (offset_res >> 4) * 4  # in bytes

        # Extract payload, goes to end of the header (data_offset) and 
        # continues to the end of the packet (where the payload actually is)
        self.payload = self.raw[self.data_offset:]

        # Decode flags into something readable
        self.flag_bits = {
            "FIN": bool(self.flags & 0x01),
            "SYN": bool(self.flags & 0x02),
            "RST": bool(self.flags & 0x04),
            "PSH": bool(self.flags & 0x08),
            "ACK": bool(self.flags & 0x10),
            "URG": bool(self.flags & 0x20),
        }

    # string representation of raw packet
    def __repr__(self):
        flags = ",".join([k for k, v in self.flag_bits.items() if v])
        return (
            f"<TCPPacket {self.src_port}→{self.dst_port} "
            f"seq={self.seq} ack={self.ack_seq} flags={flags}>"
        )