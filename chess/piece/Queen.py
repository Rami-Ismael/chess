
import pygame
from ..constant import BLACK_QUEEN, WHITE_QUEEN
from .Piece import Piece
class Queen(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
    def movement(self,board):
        return []
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_QUEEN,(self.x,self.y)) 
        else:
            screen.blit(BLACK_QUEEN,(self.x,self.y))