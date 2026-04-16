import pygame as pg
pg.init()

MARGIN = 200
VINDU_BREDDE = 700+2*MARGIN
VINDU_HOYDE = 600

WHITE = (255, 255, 255)
YELLOW = (255,255,0)
RED = (255,0,0)
BRETT_FARGE = (0,0,255)
CELLE_STR=40

SPILLER_FARGER = {"Spiller 1": RED, "Spiller 2": YELLOW}
RETTNINGER=[[-1,1],[0,1],[1,1],[1,0]]

HOVER_FARGE = (100, 100, 100)

FPS = 60

FONT = pg.font.SysFont("Arial", 72, True)