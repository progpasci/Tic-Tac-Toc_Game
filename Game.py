#! usr/bin/env

from Menu import *
from Player import *
from Board import *
import os

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")
    
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
            clearScreen()
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win or self.check_draw():
                choise = self.menu.display_end_game_menu()
                if choise == "1":
                    self.restart_game()
                else :
                    self.quit_game()
                    break
    
    def quit_game(self):
        clearScreen()
        print(("\n"*3).center(78,' '))
        print(("-"*33).center(78,' '))
        print("\t\t\t    Thank You For Playing !")
        print(("-"*33).center(78,' '))
        print(("\n"*3).center(78,' '))
        
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"\t\t\t{player.name}'s Turn ({player.symbol})") 
        while True:
            try:
                cell_choise = int(input("\t\t   Choose a cell (1 to 9) : "))
                if 1<= cell_choise <=9 and self.board.update_board(cell_choise,player.symbol):
                    break
                else :
                    print("\t\t\t   Invalid Move, Try Again.")
            except ValueError:
                print("\t\t      Please enter a number between 1 and 9")
        self.switch_player()
    
    def check_win(self):
        win_combinations = [
            [0,1,2],[3,4,5],[6,7,8], #* Rows
            [0,3,6],[1,4,7],[2,5,8], #* Columns
            [0,4,8],[2,4,6]          #* Diagonals
        ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False
    
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
        
            
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
    
game = Game()
game.start_game()
