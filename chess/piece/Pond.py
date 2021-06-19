
import pygame
from ..constant import BLACK_PAWN, WHITE_PAWN
from .Piece import Piece
class Pond(Piece):
    def __inti__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        self.pond_moves=[(1,0)]
        self.first_turn = True
        self.relative_position
        #white will alway be on the bottom 
        if color=="white":
            self.relative_position = 1
        else :
            self.relative_position = -1
        self.calc_poss()
    def movement(self):
        move = []
        if(self.first_turn):
            move.append([(self.col,self.row+1),(self.col,self.row+2)])
        return move.append([(self.col,self.row+1)
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_PAWN,(self.x,self.y)) 
        else:
            screen.blit(BLACK_PAWN,(self.x,self.y))