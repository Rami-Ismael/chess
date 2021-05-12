import pygame
from ..constant import BLACK_PAWN, SQUARE_SIZE
class Piece:
    def __init__(self,color,row_position,column_position):
        self.color
        self.board_piece
        self.row_position
        self.column_position;
        self.x=0
        self.y=0
    @abstractmethod
    def movement(self):
        pass
    #caculate the position of the x and y on the screen . 
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2
    @abstractmethod
    def draw(self,screen):
#movement will think about x and y position the 0,0 will be bottom left corner 
        
        