import pygame
from .Board import Board
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
    def draw(self):
        self.board.draw(self.win)
    def check_if_king(self,board,color):
        return True
    def turn(self,turn):
        #turn is just a color
        #get the list of valid move for the opposting playe
        return False
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()