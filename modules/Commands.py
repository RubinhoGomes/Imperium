# Description: This file contains the class Commands that will be used to handle the user input
# Author: Rubinho
# File: Commands.py

from Util import Util
from Blockchain import Blockchain
import threading
import os
import time


class Commands:
    
    def getData(message = "Enter option: "):
        option = None
            
        while type(option) != int:
            try:
                option = int(input(message))
            except Exception as e:
                Util.ErrorHandler(e)
        return option
    
    def pauseMenu():
        pause = input("Press any key to continue...")


    # TODO: Implement the necessary logic to select the correct option
    def selectOption(blockchain, option):
        if(option == 1):
            os.system("clear")
            print("Showing Blockchain")
            blockchain.printBlock()
            Commands.pauseMenu()
        elif option == 2:
            os.system("clear")
            print("Mining Block")
            blockchain.addBlock()
            blockchain.printBlock()
            Commands.pauseMenu()   
        elif option == 3:
            pass
        elif option == 4:
            print("Exiting...")
            time.sleep(2)
            exit()

    #TODO: Implement the lines to make it prettier
    # Try to make this easiear to understand and make it easier to receive just a simple int 
    def startMenu(blockchain):
        data = None
        while data != 4:
            os.system("clear")
            print("1. Show Blockchain")
            print("2. Mine Block")
            print("3. Add Transaction")
            print("4. Exit")
            data = Commands.getData()
            Commands.selectOption(blockchain, data)

    def start():
        blockchain = Blockchain()
        blockthread = threading.Thread(target=Commands.startMenu, args=(blockchain,))
        blockthread.start()
