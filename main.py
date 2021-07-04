#import

import pygame
from chess.Board import Board
from chess.constant import WIDTH,HEIGHT, SQUARE_SIZE
from chess.game import Game

FPS = 60

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")
def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
def main():
    piece_selected = []
    run = True
    clock = pygame.time.Clock()
    game = Game(win)
    game.draw()
    turn = "white"
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                print(row)
                print(col)
                if(len(piece_selected)==0):
                    if game.there_is_piece(row,col):
                        if game.return_color(row,col)==turn:
                            piece_selected.append(game.return_peice(row,col))
                            print("select a move")
                else:
                    if(game.select_move(row,col,piece_selected[0],turn)):
                        print("possible move")
                        game.update()
                        
        game.update()
main()