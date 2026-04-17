from brett import *
from konstanter import *
import pygame as pg

class Spill:
    def __init__(self, vindu:pg.Surface, brett: Brett) -> None:
        self.vindu = vindu
        self.brett = brett
        
        self.spiller = "Spiller 1"
        self.antTurer = 0
        self.noenVunnet = False
        self.fulltBrett = False
        
        self.botSinTur = None
        
    def vunnet(self):
        outline = 2
        x, y = 164 + MARGIN, 250
        tekst = f"{self.spiller} vant"
        vinnerTekst = FONT.render(tekst, True, (0, 255, 0))
        outlineTekst = FONT.render(tekst, True, (0, 0, 0))
        
        for dx, dy in [(-outline, 0), (outline, 0), (0, -outline), (0, outline), (-outline, -outline), (-outline, outline), (outline, -outline), (outline, outline)]:
            self.vindu.blit(outlineTekst, (x + dx, y + dy))
        
        self.vindu.blit(vinnerTekst, (x, y))
        
    def uavgjort(self):
        outline = 2
        x, y = 229 + MARGIN, 250
        tekst = f"Uavgjort"
        uavgjortTekst = FONT.render(tekst, True, (0, 255, 0))
        outlineTekst = FONT.render(tekst, True, (0, 0, 0))
        
        for dx, dy in [(-outline, 0), (outline, 0), (0, -outline), (0, outline), (-outline, -outline), (-outline, outline), (outline, -outline), (outline, outline)]:
            self.vindu.blit(outlineTekst, (x + dx, y + dy))
        
        self.vindu.blit(uavgjortTekst, (x, y))
        
        
    def plasserBrikke(self, kol):
        for r in self.brett.brett[kol]:
            if r.farge == HOVER_FARGE or r.farge == WHITE:
                r.farge = SPILLER_FARGER[self.spiller]
                if self.brett.sjekkSeier(r):
                    print(f"{self.spiller} har vunnet")
                    self.noenVunnet = True
                    return
                self.spiller = "Spiller 2" if self.spiller == "Spiller 1" else "Spiller 1"
                self.antTurer += 1
                if self.antTurer >= 42:
                    self.fulltBrett = True
                return
    
    def spillerPlasserBrikke(self, event:pg.Event,):
                mx, my = event.pos
                mx -= MARGIN
                kol = mx//100
                if kol >= 0 and kol <= 6:
                    try:
                        self.plasserBrikke(kol) #type: ignore
                    except:
                        pass
    
    def spillMotBot(self):
        if input("Vil du spille mot en bot? y/n\n") == "y":
            if int(input("Skal botten være spiller 1 eller 2? 1/2\n")) == 1:
                self.botSinTur = "Spiller 1"
            else:
                self.botSinTur = "Spiller 2"
            return True
        return False
    
    def gameState(self):
        if self.noenVunnet:
            self.vunnet()
        elif self.fulltBrett:
            self.uavgjort()