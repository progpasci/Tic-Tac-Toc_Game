#! usr/bin/env
import os
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    def choose_name(self):
        while True:
            name = input("\t\t      Enter Your Name (Letters Only) : ")
            if name.isalpha():
                self.name = name
                break
            os.system("cls")
            print(("-"*33).center(78,' '))
            print("\t\t   Invalid Name. Please use (Letters Only): ")
            print(("-"*33).center(78,' '))
    def choose_symbol(self):
        while True:
            symbol = input(f"\t\t  {self.name}, Choose Your Symbol (A Single Letter) : ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            
            os.system("cls")
            print(("-"*33).center(78,' '))
            print("\t\tInvalid Symbol. Please Choose (A Single Letter): ")
            print(("-"*33).center(78,' '))