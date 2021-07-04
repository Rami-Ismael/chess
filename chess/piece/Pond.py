
import pygame
from ..constant import BLACK_PAWN, WHITE_PAWN
from .Piece import Piece
from .pieces import pieces
from ..move import move
class Pond(Piece):
    def __init__(self,color,row_position,column_position):
        super().__init__(color,row_position,column_position)
    def movement(self,board):
        moves = []
        current_col = self.col
        current_row = self.row
        future_row = self.row+1
        future_col = self.col
        the_piece = 1 * self.integer_value
        took_a_peice = False
        piece_taken = 0
        moves.append(move(current_col,current_row,future_row,future_col,the_piece,took_a_peice,piece_taken))
        return moves
    def draw(self,screen):
        if self.color =="white":
            screen.blit(WHITE_PAWN,(self.x,self.y)) 
        else:
            screen.blit(BLACK_PAWN,(self.x,self.y))