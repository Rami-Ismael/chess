
import pygame
from ..constant import WHITE_KING, BLACK_KING
from ..move import move
from .Piece import Piece
class King(Piece):
    def __inti__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
        self.king_moves=[(1,1),(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1)]
        self.calc_poss()
    def movement(self,board):
        valid_move = []
        for vetor in king_moves:
            dr = self.row+vector[1]
            dc = self.col+vector[0]
            if(dr>=0 and dr<8 and dc>=0 and dc<8):
                if(board[dr][dc]==0):
                    valid_moves.append(move(self.row,self.col,dr,dc,"King",False,null))
                elif board[dr][dc].color!=self.color:
                    valid_moves.append(move(self.row,self.col,dr,dc,"King",True,))
                    
                    
        return self.pond_moves[0]
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_KING,(self.x,self.y)) 
        else:
            screen.blit(BLACK_KING,(self.x,self.y))