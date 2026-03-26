from hashlib import sha256

class Util:
    
    @staticmethod
    def checkTransactionPair(Transaction):
      ## Check if the transaction is even or odd, if even return True, if odd return False
        return True if len(Transaction) % 2 == 0 else False
        
    @staticmethod
    def calculateBothHash(transactionA, transactionB):
        transactionA = Util.calculaTransactionHash(transactionA)
        transactionB = Util.calculaTransactionHash(transactionB)
        return sha256(str(transactionA + transactionB).encode()).hexdigest()
        
    @staticmethod
    def calculaTransactionHash(transaction):
        return sha256(str(transaction).encode()).hexdigest()
    
    @staticmethod
    def calculateHash(*args) -> str:
        return sha256(str(args).encode()).hexdigest()

    @staticmethod
    def ErrorHandler(exception):
        print(exception)
        print("An error has occurred, please try again")
        pause = input("Press any key to close the app...")
        exit()

    @staticmethod
    def get_free_port():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 0))
        port = s.getsockname()[1]
        s.close()
        return port


    @staticmethod
    def get_saved_state():
        import json
        try:
            with open('state.json', 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return None
