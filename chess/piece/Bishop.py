import pygame
from ..constant import WHITE_BISHOP, BLACK_BISHOP
from .Piece import Piece

class Bishop(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
    def movement(self,board):
        valid_moves = []
        return []
        for row_direction in(1,-1):
            for col_direction in (1,-1):
                blocking = True
                for vector in self.bishop_moves and blocking:
                    dr = self.row+vector[1]*row_direction
                    dc = self.col + vector[0]*col_direction
                    if(dr<8 and dc >=0 and dc >=0 and dc<8):
                        if board[dr][dc]==0 :
                            valid_moves.append((dc,dr))
                    else:
                            valid_moves.append((dc,dr))
                            blocking = False
        return valid_moves

    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_BISHOP,(self.x,self.y)) 
        else:
            screen.blit(BLACK_BISHOP,(self.x,self.y))