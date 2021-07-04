import pygame
import abc
from ..constant import BLACK_PAWN, SQUARE_SIZE
class Piece(metaclass=abc.ABCMeta):
    def __init__(self,color,row_position,column_position):
        self.color = color
        ##sself.board_piece 
        self.row = row_position
        self.col = column_position
        self.x=0
        self.y=0
        self.integer_value = 0
        if color=="white":
            self.integer_value = 1
        else:
            self.integer_value=-1
        self.calc_pos()
        self.bishop_moves=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]
        self.first_turn = True
        self.king_moves=[(1,1),(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1)]
    @abc.abstractmethod 
    def movement(self,board):
       return  
    #caculate the position of the x and y on the screen . 
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col  
        self.y = SQUARE_SIZE * self.row  
    @abc.abstractmethod 
    def draw(self,screen):
        return
#movement will think about x and y position the 0,0 will be bottom left corner 