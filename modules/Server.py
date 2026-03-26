import socket
from Network import Network, NetState

#TODO:[] Create the necessary methods to integrate the blockchain with client and server.
#     [] No need to get to fancy, just make it work.
#     [] If needed use the network file to implement repetitive methods. Like connect and IP
#     [] Handling, The server should be able to handle multiple clients
#     [] The client will be accepted and send a "Need Blockchain" ping, and a "Create Me" ping
#     [] This method garrantes that the server will handle the client and create a User and Hash
#     [] The Hash will be used to identify the user and assign the transaction to his hash
#     [] The user will be able to see his transactions and the blockchain
#     [] With this changes, we can now add transactions to the "new block" this "personal"
#     [] transactions will be added to a "pending" list, and will be added to the next mined block
#     [] Some methods probably will need. GetAllUsers, GetUserHash
class Server():

    def server():
        # Create a socket object
        s = Network.socket

        # Bind to the port
        s.bind((Network.host, Network.port))

        # Now wait for client connection.
        s.listen(5)

        print('Server listening....')

        # Establish connection with client.
        conn, addr = s.accept()
        print('Got connection from', addr)

        while True:
            #conn.send('Thank you for connecting'.encode())
            conn.send(str(NetState.PING).encode())
            # Receive the data           
            data = conn.recv(Network.size)
            print(data.decode())

           # Close the connection
        c.close()


    if __name__ == '__main__':
        server()
