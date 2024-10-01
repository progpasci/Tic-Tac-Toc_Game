#! usr/bin/env

from Menu import *
from Player import *
from Board import *
import os
class Game:
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
        
    def start_game(self):
        choise = self.menu.display_main_menu()
        if choise == "1":
            self.setup_players()
            self.play_game()
        else :
            self.quit_game()
    
    def setup_players(self):
        for index, player in enumerate(self.players,start=1):
            print(f"\t\t      Player [{index}], Enter Your Details : ")
            player.choose_name()
            player.choose_symbol()
            os.system("cls")
    
    def play_game(self):
        pass
    
    def quit_game(self):
        pass
    
    
game = Game()
game.start_game()
