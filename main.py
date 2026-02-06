import pygame as pg 
from konstanter import *
from brett import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

font = pg.font.SysFont("Arial", 72, True)

brett = Brett()

def main():
    running = True
    noenVunnet: bool = False
    fulltBrett: bool = False
       
    spiller: str = "Spiller 1"
    
    antTurer = 0
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not noenVunnet:
                mx, my = event.pos
                mx -= MARGIN
                kol = mx//100
                if kol >= 0 and kol <= 6:
                    try:
                        noenVunnet, spiller = plasserBrikke(spiller, kol) #type: ignore
                        antTurer += 1
                        if antTurer >= 42:
                            fulltBrett = True
                    except:
                        pass

        vindu.fill(BRETT_FARGE)
        
        hover(brett)
                            
        brett.draw(vindu)
        
        if noenVunnet:
            vunnet(spiller)
        elif fulltBrett:
            uavgjort()
        
        pg.display.flip()
        clock.tick(FPS)


def vunnet(spiller):
    outline = 2
    x, y = 164 + MARGIN, 250
    tekst = f"{spiller} vant"
    vinnerTekst = font.render(tekst, True, (0, 255, 0))
    outlineTekst = font.render(tekst, True, (0, 0, 0))
    
    for dx, dy in [(-outline, 0), (outline, 0), (0, -outline), (0, outline), (-outline, -outline), (-outline, outline), (outline, -outline), (outline, outline)]:
        vindu.blit(outlineTekst, (x + dx, y + dy))
    
    vindu.blit(vinnerTekst, (x, y))
    
def uavgjort():
    outline = 2
    x, y = 229 + MARGIN, 250
    tekst = f"Uavgjort"
    uavgjortTekst = font.render(tekst, True, (0, 255, 0))
    outlineTekst = font.render(tekst, True, (0, 0, 0))
    
    for dx, dy in [(-outline, 0), (outline, 0), (0, -outline), (0, outline), (-outline, -outline), (-outline, outline), (outline, -outline), (outline, outline)]:
        vindu.blit(outlineTekst, (x + dx, y + dy))
    
    vindu.blit(uavgjortTekst, (x, y))
    
    
def plasserBrikke(spiller, kol):
    for r in brett.brett[kol]:
        if r.farge == HOVER_FARGE or r.farge == WHITE:
            r.farge = SPILLER_FARGER[spiller]
            if brett.sjekkSeier(r):
                print(f"{spiller} har vunnet")
                return True, spiller
            spiller = "Spiller 2" if spiller == "Spiller 1" else "Spiller 1"
            return False, spiller
    
if __name__ == "__main__":
    main()