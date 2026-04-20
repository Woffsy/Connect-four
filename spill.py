from brett import *
from konstanter import *
from knapper import *
import pygame as pg

class Spill:
    def __init__(self, vindu:pg.Surface, brett: Brett) -> None:
        self.vindu = vindu
        self.brett = brett
        
        self.spiller = "Spiller 1"
        self.antTurer:int = 0
        self.noenVunnet:bool = False
        self.fulltBrett:bool = False
        
        self.botSinTur:str|None = None
        
        self.startet:bool = False
        
        self.meny:list[Knapp] = []
        self.meny.append(Knapp(400, 250, "Ja"))
        self.meny.append(Knapp(550, 250, "Nei"))
        
        self.tekst:str = f"Vil du spille mot en bot?"
        self.tekstX:int = 200
        
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
        pg.draw.rect(self.vindu, BRETT_FARGE, (0, 0, VINDU_BREDDE, VINDU_HOYDE))
        outline = 2
        tekst = FONT.render(self.tekst, True, (0, 255, 0))
        outlineTekst = FONT.render(self.tekst, True, (0, 0, 0))
        
        for dx, dy in [(-outline, 0), (outline, 0), (0, -outline), (0, outline), (-outline, -outline), (-outline, outline), (outline, -outline), (outline, outline)]:
            self.vindu.blit(outlineTekst, (self.tekstX + dx, 40 + dy))
        
        self.vindu.blit(tekst, (self.tekstX, 40))
        
        for knapp in self.meny:
            knapp.tegn(self.vindu, WHITE)
    
    def spillMotBotEvent(self, event: pg.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for knapp in self.meny:
                if event.type == pg.MOUSEBUTTONDOWN and knapp.rektangel.collidepoint(event.pos):
                    if knapp.tekst == "Ja":
                        self.meny = []
                        self.meny.append(Knapp(200, 250, "Spiller 1"))
                        self.meny.append(Knapp(550, 250, "Spiller 2"))
                        self.tekst = f"Hvilken spiller skal botten være?"
                        self.tekstX = 100
                        
                    elif knapp.tekst == "Nei":
                        self.startet = True
                        
                    elif knapp.tekst == "Spiller 1":
                        self.botSinTur = "Spiller 1"
                        self.startet = True
                        return "Spiller 1"
                    
                    elif knapp.tekst == "Spiller 2":
                        self.startet = True
                        self.botSinTur = "Spiller 2"
                        return "Spiller 2"

    def gameState(self):
        if self.noenVunnet:
            self.vunnet()
        elif self.fulltBrett:
            self.uavgjort()