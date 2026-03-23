def main():
    print("Hello from cs333-network-utils-temp-name!")


if __name__ == "__main__":
    main()

class Packet:
    # TODO: Implement the Packet class with appropriate attributes and methods
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Packet(data={self.data})"