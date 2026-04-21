import pygame as pg
from konstanter import *

class Knapp:
    """Klasse for å representere en knapp"""
    def __init__(self, xPosisjon, yPosisjon, tekst):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.bredde = len(tekst) * 36 + 20
        self.hoyde = 80
        self.tekst = tekst
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde
        )

    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rektangel)
        tekst = FONT.render(self.tekst, True, BLACK)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        vindu.blit(tekst, tekstRamme.topleft)

class RestartKnapp(Knapp):
    def __init__(self, xPosisjon, yPosisjon, tekst):
        super().__init__(xPosisjon, yPosisjon, tekst)
        self.bredde = len(tekst) * 24 + 10
        self.hoyde = 60
        self.tekst = tekst
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde
        )
    
    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rektangel)
        tekst = FONTRESTART.render(self.tekst, True, BLACK)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        vindu.blit(tekst, tekstRamme.topleft)