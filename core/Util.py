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

