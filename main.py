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



# write var to disk in binary format
def to_bin(var):
    # step 1: convert var to hex format
    num = int(var).to_bytes(1, byteorder='big')
    # step 2: write var in binary to file
    with open("test.bin", "wb") as f:
        f.write(num)


# read binary file from memory 
def from_bin():
    # step 1: read from a binary file
    f = open("test.bin", "rb")
    bin = f.read()
    f.close()
    # step 2: convert binary to integer
    return int.from_bytes(bin, byteorder='big')

# convert ip address to binary and write to file
def ip_to_file(ip):
    with open("ip.bin", "wb") as f:
        for num in ip.split('.'):
            f.write(int(num).to_bytes(1, byteorder='big'))

# read binary file and convert to ip address
def file_to_ip():
    with open("ip.bin", "rb") as f:
        ip_bytes = f.read()
        ip_parts = [str(int.from_bytes(ip_bytes[i:i+1], byteorder='big')) for i in range(4)]
        return '.'.join(ip_parts)

if __name__ == "__main__":
    # main()
    # our implementation
    ip = "197.168.0.1"
    ip_split = ip.split('.')
    for num in ip_split:
        to_bin(num)
        var = from_bin()
        print(var)
    
    # professor inspired implementation
    ip_to_file(ip)
    print(file_to_ip())

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
