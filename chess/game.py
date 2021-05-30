from .Board import Board
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
    def draw(self):
        self.board.draw(self.win)
