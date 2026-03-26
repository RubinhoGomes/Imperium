from dataclasses import dataclass

@dataclass
class Transaction():
    sender: str
    receiver: str
    amount: int
    
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self. receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"Sender: {self.sender}, Receiver: {self.receiver}, Amount: {self.amount} Rublito"

