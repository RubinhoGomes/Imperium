from Block import Block

class Blockchain(Block):
    def __init__(self):
        self.block = [Block(['Genesis Block'], [], 0, 0, 0)]
        self.difficulty = 1

    def __post_init__(self):
        self.hash = self.calculateHash()
        self.previousHash = "Genesis Block"
        self.nonce = 0
        self.difficulty = 1
        self.index = 0

    def addBlock(self):
        block = Block(self.block[-1].hash, [], self.block[-1].nonce+1, self.block[-1].index+1)
        block.mineBlock(self.difficulty)
        self.block.append(block)

    def printBlock(self):
        for b in self.block:
            print(b)

    def getLastIndex(self) -> int:
        return len(self.block) - 1

