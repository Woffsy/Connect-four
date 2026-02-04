import pygame as pg 
from konstanter import *
from brett import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

brett = Brett()

def main():
    running = True
       
    spiller = "spiller1"
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for r in brett.brett[mx//100]:
                    if r.farge == WHITE:
                        r.farge = SPILLER_FARGER[spiller] 
                        if spiller == "spiller1":
                            spiller = "spiller2"
                        elif spiller == "spiller2":
                            spiller = "spiller1"
                        break

        vindu.fill(BRETT_FARGE)
        
        brett.draw(vindu)
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()