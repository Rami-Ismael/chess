import pygame

WIDTH,HEIGHT = 800,800

ROWS, COLS  = 8,8

SQUARE_SIZE = WIDTH//COLS

RED = (255,0,0)
WHITE = (255,255,255)
BLACK  = (0,0,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
LIGHT_BROWN = (224,139,62)
BRIGHT_WHITE = (251,241,231)

## piece
BLACK_PAWN_PATH = "/home/rami/code/chess/chess/piece/assets/black_pawn.png"
BLACK_PAWN = pygame.transform.scale(pygame.image.load(BLACK_PAWN_PATH),(SQUARE_SIZE,SQUARE_SIZE))
