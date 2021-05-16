
import pygame
from ..constant import WHITE_ROOK, BLACK_ROOK
from .Piece import Piece
class Rook(Piece):
    def __inti__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        self.pond_moves=[(1,0)]
        self.relative_position
        #white will alway be on the bottom 
        if color=="white":
            self.relative_position = 1
        else :
            self.relative_position = -1
        self.calc_poss()
    def movement(self):
        return self.pond_moves[0]
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_ROOK,(self.x,self.y)) 
        else:
            screen.blit(BLACK_ROOK,(self.x,self.y))