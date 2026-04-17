import pygame as pg 
from konstanter import *
from brett import *
from bot import *
from spill import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

brett = Brett()

spill = Spill(vindu, brett)

def main():
    running = True

    botSinTur = None
    bot = None

    if input("Vil du spille mot en bot? y/n\n") == "y":
        if int(input("Skal botten være spiller 1 eller 2? 1/2\n")) == 1:
            botSinTur = "Spiller 1"
        else:
            botSinTur = "Spiller 2"
        bot = Bot(botSinTur, brett, spill)
       
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not spill.noenVunnet and spill.spiller != botSinTur:
                spill.spillerPlasserBrikke(event)

        if spill.spiller == botSinTur and not spill.noenVunnet and bot:
            bot.botTrekk()
        
        vindu.fill(BRETT_FARGE)
        
        hover(brett)
                            
        brett.draw(vindu)
        if spill.noenVunnet:
            spill.vunnet()
        elif spill.fulltBrett:
            spill.uavgjort()
        
        pg.display.flip()
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()