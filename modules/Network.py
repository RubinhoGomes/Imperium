import socket
from dataclasses import dataclass



class NetState:
    PING = 0 #TODO: [] Implement this ping to check if the server is up
    PONG = 1 #TODO: [] Implement this pong to check if the client is up
    CONNECT = 2 #TODO: [] Implement this to Create an user and his hash and send Blockchain Ping
    DISONNECT = 3 #TODO: [] Implement this to disconnect the user
    MINE = 3 #TODO: [] Implement this to mine the block
    BLOCKCHAIN = 4 #TODO: [] Send the blockchain through the network
    TRANSACTION = 5 #TODO: [] Send the transaction through the network
    TRANSACTION_ADD = 6 #TODO: [] Begin the add an transaction process, The user will choose from a list the user ID after will choose the amount and FINISH
    TRANSACTION_VIEW = 7 #TODO: [] Will show all the user pending transactions, or don't know how to show all the transactions, but probably "locally"

class Network:
    size = 1024
    host = socket.gethostname()
    port = 12345
    socket = socket.socket()

