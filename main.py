import pygame as pg 
from konstanter import *
from brett import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

brett = Brett()

def main():
    running = True
    brett.brett[6][0].farge = RED
    brett.brett[6][1].farge = RED
    brett.brett[2][0].farge = RED
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(BRETT_FARGE)
        
        brett.draw(vindu)
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()