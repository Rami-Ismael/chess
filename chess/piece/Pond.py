
import pygame
from ..constant import BLACK_PAWN, WHITE_PAWN
from .Piece import Piece
from .pieces import pieces
class Pond(Piece):
    def __inti__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        self.pond_moves=[(1,0)]
        self.first_turn = True
        self.relative_position
        #white will alway be on the bottom 
        if color=="white":
            self.r
        else :
            self.relative_position = -1
        self.calc_poss()
    def movement(self,board):
        move = []
        move.append(move((self.col,self.row,self.col,self.row+1*self.interger_value,self.col,self.interger_value*1,False,0)))
        if(self.first_turn):
            move.append(move((self.col,self.row,self.col,self.row+2*self.interger_value,self.col,self.interger_value*1,False,0)))
        return move
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_PAWN,(self.x,self.y)) 
        else:
            screen.blit(BLACK_PAWN,(self.x,self.y))