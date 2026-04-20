import pygame as pg 
from konstanter import *
from brett import *
from bot import *
from spill import *
from knapper import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

brett = Brett()

spill = Spill(vindu, brett)

def main():
    running = True
    bot = None
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif not spill.startet:
                if spill.spillMotBotEvent(event) in ("Spiller 1", "Spiller 2"):
                    bot = Bot(brett, spill)
            elif event.type == pg.MOUSEBUTTONDOWN and not spill.noenVunnet and spill.spiller != spill.botSinTur and spill.startet:
                spill.spillerPlasserBrikke(event)

        if spill.spiller == spill.botSinTur and not spill.noenVunnet and bot and spill.startet:
            bot.botTrekk()
        
        vindu.fill(BRETT_FARGE)
        
        hover(brett)
                            
        brett.draw(vindu)
        spill.gameState()
        if not spill.startet:
            spill.spillMotBot()

        
        pg.display.flip()
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()