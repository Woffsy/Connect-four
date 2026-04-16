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
    noenVunnet: bool = False
    fulltBrett: bool = False

    spiller: str = "Spiller 1"

    botSinTur = None

    if input("Vil du spille mot en bot? y/n\n") == "y":
        bot = Bot(spiller, brett)
        if int(input("Skal botten være spiller 1 eller 2? 1/2\n")) == 1:
            botSinTur = "Spiller 1"
        else:
            botSinTur = "Spiller 2"
       
    
    antTurer = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not noenVunnet and spiller != botSinTur:
                mx, my = event.pos
                mx -= MARGIN
                kol = mx//100
                if kol >= 0 and kol <= 6:
                    try:
                        noenVunnet, spiller = spill.plasserBrikke(spiller, kol) #type: ignore
                        antTurer += 1
                        if antTurer >= 42:
                            fulltBrett = True
                    except:
                        pass

        if spiller == botSinTur:
            bot.botTrekk() #type: ignore
        
        vindu.fill(BRETT_FARGE)
        
        hover(brett)
                            
        brett.draw(vindu)
        
        if noenVunnet:
            spill.vunnet(spiller)
        elif fulltBrett:
            spill.uavgjort()
        
        pg.display.flip()
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()