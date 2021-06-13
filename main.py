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
    
    run = True
    clock = pygame.time.Clock()
    game = Game(win)
    game.draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
        game.update()
main()