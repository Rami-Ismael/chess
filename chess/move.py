
from chess.piece.pieces import pieces
class move:
    def __init__(self,current_row,current_col,future_row,future_col,piece,took_a_piece,piece_taken):
        self.current_row = current_row
        self.current_col = current_col
        self.future_row = future_row
        self.future_col = future_col
        self.piece = pieces(piece)
        self.took_a_piece = took_a_piece
        self.piece_taken  = 0
