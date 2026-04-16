from brett import *
from konstanter import *
import pygame as pg

class Spill:
    def __init__(self, vindu:pg.Surface, brett: Brett) -> None:
        self.vindu = vindu
        self.brett = brett
    def vunnet(self, spiller):
        outline = 2
        x, y = 164 + MARGIN, 250
        tekst = f"{spiller} vant"
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
        
        
    def plasserBrikke(self, spiller, kol):
        for r in self.brett.brett[kol]:
            if r.farge == HOVER_FARGE or r.farge == WHITE:
                r.farge = SPILLER_FARGER[spiller]
                if self.brett.sjekkSeier(r):
                    print(f"{spiller} har vunnet")
                    return True, spiller
                spiller = "Spiller 2" if spiller == "Spiller 1" else "Spiller 1"
                return False, spiller