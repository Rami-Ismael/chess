
import pygame
from ..constant import WHITE_ROOK, BLACK_ROOK
from .Piece import Piece
class Rook(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        
    def movement(self,board):
        return []
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_ROOK,(self.x,self.y)) 
        else:
            screen.blit(BLACK_ROOK,(self.x,self.y))