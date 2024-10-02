#! usr/bin/env
class Board :
    def __init__(self) -> None:
        self.board = []
        self.board = [str(i) for i in range(1,10)] #(List Comprehension)
        # for i in range(1,10): self.board.append(str(i))
        
    def display_board(self):
        print()
        for i in range(0,9,3):
            print((" "*25),end=' ')
            print(" | ".join(self.board[i:i+3]))
            if i < 6 : 
                print((" "*25),end=' ')
                print("- "*5)
        print()
                
    def update_board(self,choise,symbol):
        if self.is_valid_move(choise):
            self.board[choise -1] = symbol
            return True
        return False
    
    def is_valid_move(self,choise):
        return self.board[choise -1].isdigit()
    
    def reset_board(self):
        for i in range(1,10): self.board.append(str(i))
            