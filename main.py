from tcp_parser import TCPPacketParser

def main():
    print("Hello from cs333-network-utils-temp-name!")
    fake_packet = (
        b"\x30\x39"      # src port = 12345
        b"\x00\x50"      # dst port = 80
        b"\x12\x34\x56\x78"  # seq number
        b"\x00\x00\x00\x00"  # ack number
        b"\x50"          # data offset (5) << 4
        b"\x02"          # flags (SYN)
        b"\xfa\xf0"      # window size
        b"\x00\x00"      # checksum (fake)
        b"\x00\x00"      # urgent pointer
        b"hello"         # payload
    )
    
    packet = TCPPacketParser(fake_packet)
    print("source port:", packet.src_port)
    print("destination port:", packet.dst_port)
    print("flags:", packet.flag_bits)
    print("payload:", packet.payload)

if __name__ == "__main__":
    main()

class Packet:
    # TODO: Implement the Packet class with appropriate attributes and methods
    def __init__(self, src_ip, dst_ip, src_port, dst_port, data):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port

        self.seq = 0x11111111 # sequence number
        self.ack_seq = 0 # acknowledgment number
        self.window = 64240 # window size
        self.payload = data # payload data
