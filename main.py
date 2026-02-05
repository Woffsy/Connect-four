import pygame as pg 
from konstanter import *
from brett import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

font = pg.font.SysFont("Arial", 48, True)

brett = Brett()

def main():
    running = True
    noenVunnet = False
       
    spiller = "Spiller 1"
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for r in brett.brett[mx//100]:
                    if r.farge == HOVER_FARGE or r.farge == WHITE:
                        r.farge = SPILLER_FARGER[spiller]
                        if brett.sjekkSeier(r):
                            noenVunnet = True
                            print(f"{spiller} har vunnet")
                            break
                        spiller = "Spiller 2" if spiller == "Spiller 1" else "Spiller 1"
                        break

        vindu.fill(BRETT_FARGE)
        
        hover(brett)
                            
        brett.draw(vindu)
        
        if noenVunnet:
            vinnerTekst = font.render(f"{spiller} vant", True, (0, 0, 0))
            vindu.blit(vinnerTekst, (100, 100))
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()