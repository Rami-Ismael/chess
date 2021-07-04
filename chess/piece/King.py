
import pygame
from ..constant import WHITE_KING, BLACK_KING
from ..move import move
from .Piece import Piece
class King(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
    def movement(self,board):
        valid_move = []
        for vector in self.king_moves:
            print(vector)
            dr = self.row+vector[1]
            dc = self.col+vector[0]
            if(dr>=0 and dr<8 and dc>=0 and dc<8):
                if(board[dr][dc]==0):
                    valid_move.append(move(self.row,self.col,dr,dc,"King",False,0))
                elif board[dr][dc].color!=self.color:
                    valid_move.append(move(self.row,self.col,dr,dc,"King",True,0))
                    
                    
        return valid_move
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_KING,(self.x,self.y)) 
        else:
            screen.blit(BLACK_KING,(self.x,self.y))