from dataclasses import dataclass, field
import Transaction
from Util import Util



@dataclass
class User():
    id: int 
    name: str
    hash: str = field(init=False)
    balance: float = 0.0
    pending: float = 0.0
    transactions: list() = field(init=False)

    def __post_init__(self):
        self.hash = Util.calculateHash([str(self.id).encode, str(self.name).encode, str(self.balance).encode, str(self.pending).encode])
        self.transactions = []

    def __str__(self):
        return f"Username: {self.name}\nBalance: {self.balance}\nPending: {self.pending}\n"

    def addTransaction(self, transaction):
        self.transactions.append(transaction)


user = User(1, "Rubinho")

print(user)

user.transactions.append(Transaction.Transaction(1, 2, 10.0))

print(user)
