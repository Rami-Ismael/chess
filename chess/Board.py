import pygame
from .constant import BRIGHT_WHITE,ROWS,COLS,LIGHT_BROWN,SQUARE_SIZE
class Board:
    def __init__(self):
        self.board=[]
    def draw_square(self,win):
        win.fill(BRIGHT_WHITE)
        for row in range(ROWS):
            for col in range(row%2,ROWS,2):
                pygame.draw.rect(win,LIGHT_BROWN,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
        