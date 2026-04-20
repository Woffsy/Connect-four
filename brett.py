import pygame as pg
from konstanter import *

class Rute:
    def __init__(self, rad:int, kol:int, str:int) -> None:
        self.rad = rad
        self.kol = kol
        self.str = str
        
        self.hover = False
        self.farge: tuple = WHITE
        
        
    def draw(self, vindu):
        if self.hover and self.farge == WHITE:
            self.farge = HOVER_FARGE
        elif not self.hover and self.farge == HOVER_FARGE:
            self.farge = WHITE
        elif self.farge in SPILLER_FARGER:
            self.hover = False
        pg.draw.circle(vindu, self.farge, (self.kol*100+50+MARGIN, VINDU_HOYDE-self.rad*100-50), CELLE_STR)

class Brett:
    def __init__(self) -> None:
        self.ant_rad:int = 6
        self.ant_kol:int = 7
        self.celle_str = CELLE_STR
        
        self.brett = [[Rute(r, k, self.celle_str) for r in range(self.ant_rad)] for k in range(self.ant_kol)]
    
    def draw(self, vindu):
        for kol in range(self.ant_kol):
            for rad in range(self.ant_rad):
                self.brett[kol][rad].draw(vindu)
    
    def sjekkSeier(self, rute:Rute):
        
        for r in RETTNINGER:
            antPåRad=0
            for s in range(-3,4):
                if rute.kol+s*r[0] in range(0,7) and rute.rad+s*r[1] in range(0,6):
                    antPåRad=antPåRad+1 if self.brett[rute.kol+s*r[0]][rute.rad+s*r[1]].farge == rute.farge else 0
                    if antPåRad>=4:
                        return True
            
        
                
def hover(brett):
    mx2, my2 = pg.mouse.get_pos()
    mx2 -= MARGIN
    kol = mx2//100
    if kol >= 0 and kol <= 6:
        for r in brett.brett[kol]:
            if r.farge == WHITE or r.farge == HOVER_FARGE:
                r.hover = True
                break
        
    for i, k in enumerate(brett.brett):
        if i != kol:
            for r in k:
                r.hover = False