import pygame
from .constant import BRIGHT_WHITE,ROWS,COLS,LIGHT_BROWN,SQUARE_SIZE
from .piece.Pond import Pond
WHITE_SECTION = "white"
BLACK_SECTION = "black"
class Board:
    def __init__(self):
        self.board=[]
    def draw_square(self,win):
        win.fill(BRIGHT_WHITE)
        for row in range(ROWS):
            for col in range(row%2,ROWS,2):
                pygame.draw.rect(win,LIGHT_BROWN,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
        
    def create_board(self):
        #create a board using the list data structure in python
        for row in range(ROWS):
            self.board.append([])
            for col in range( COLS):
               if row==1 :
                    self.board[row].append(Pond(WHITE_SECTION,row,col))
               else:
                   self.board[row].append(0)
    def get_piece(self,row,col):
        return self.board[row][col]
    def draw(self,win):
        self.draw_square(win)
        self.create_board()
        for row in range (ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    piece = self.get_piece(row,col)
                    print(piece.x)
                    print(piece.y)
                    self.board[row][col].draw(win)
        