import pygame
from .Board import Board
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
        self.white_pieces = []
        self.black_peice = []
        for x in self.board.board:
            if(x!=0):
                if(x.color=="white"):
                    white_pieces.append(x)
                else:
                    black_peice.append(x)
            
    def draw(self):
        self.board.draw(self.win)
    def check_if_king(self,board,color):
        return False
    def valid_moves(self,turn):
        valid_moves = []
        #turn is just a color
        #get the list of valid move for the opposting playe
        if turn=="white":
            print(self.white_pieces)
            for x in self.white_pieces:
                print(x)
                valid_moves+=x.movement()
        else:
            for x in self.white_pieces:
                valid_moves+=x.movement()
        
        return valid_moves
    def select_move(self,row,col,piece,turn):
        valid_moves = self.valid_moves(turn)
        print(valid_moves)
        for x in valid_moves:
            if x.piece==piece.integer_value:
                if x.row ==row and x.col ==col:
                    return True
        return False
    def return_move(self,row,col,piece):
        valid_moves = self.valid_moves
        for x in valid_moves:
            if x.piece==piece.integer_value:
                if x.row ==row and x.col ==col:
                    return x
        return 
    def there_is_piece(self,row,col):
        if self.board.board[row][col] !=0:
            return True
        return  False
    def return_color(self,row,col):
        if self.board.board[row][col]!=0:
            return self.board.board[row][col].color
        return 
    def return_peice(self,row,col):
        return self.board.board[row][col]
    def update_board(self,row,col):
        return 5
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()