#import

import pygame
from chess.Board import Board
from chess.constant import WIDTH,HEIGHT

FPS = 60

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")

def main():
    
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(win)
        pygame.display.update()
main()