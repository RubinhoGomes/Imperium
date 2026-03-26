from Network import Network, NetState
import socket
import sys

class Client():

    def client():
        # Create a socket object
        s = Network.socket

        # Connect to the server
        s.connect((Network.host, Network.port))

        while True:
            data = s.recv(Network.size)
            print(data.decode())
            print(sys.getsizeof(data.decode()))

        s.close()

    if __name__ == '__main__':
        client()
