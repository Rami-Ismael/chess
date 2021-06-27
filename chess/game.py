import pygame
from .Board import Board
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
        white_pieces = []
        black_peice = []
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
    def turn(self,turn):
        #turn is just a color
        #get the list of valid move for the opposting playe
        if turn=="white" :
            for
        return False
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()