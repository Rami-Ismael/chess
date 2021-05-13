import pygame
from abc import ABC,abstractmethod
from ..constant import BLACK_PAWN, SQUARE_SIZE
class Piece(ABC):
    def __init__(self,color,row_position,column_position):
        self.color = color
        ##sself.board_piece 
        self.row = row_position
        self.col = column_position
        self.x=0
        self.y=0
        self.calc_pos()
    @abstractmethod
    def movement(self):
        pass
    #caculate the position of the x and y on the screen . 
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2
    @abstractmethod
    def draw(self,screen):
        return
#movement will think about x and y position the 0,0 will be bottom left corner 