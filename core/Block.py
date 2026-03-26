from dataclasses import dataclass, is_dataclass
import Transaction
import hashlib

@dataclass
class Block():
    transaction: list[Transaction]
    previousHash: str
    hash: str
    nonce: int
    index: int

    def __post_init__(self):
        self.hash = self.calculateHash()

    def calculateHash(self) -> str:
        return hashlib.sha256(str(self.previousHash).encode() + str(self.nonce).encode()).hexdigest()

    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
        # Todo make this automatic
        self.transaction.append()
        print("Block mined: " + self.hash)

    def createTransaction(sender, receiver, amount):
        transaction = Transaction.Transaction(sender, receiver, amount)
        return transaction

    def __str__(self) -> str:
        return f"Block {self.index}\nPrevious Hash: {self.previousHash} \nHash: {self.hash} \nNonce: {self.nonce}\n---"

print(Block.createTransaction(22, 22, 1))
