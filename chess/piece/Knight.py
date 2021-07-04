import pygame
from ..constant import WHITE_KNIGHT, BLACK_KNIGHT
from .Piece import Piece

class Knight(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
    def movement(self,board):
        return []
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_KNIGHT,(self.x,self.y)) 
        else:
            screen.blit(BLACK_KNIGHT,(self.x,self.y))