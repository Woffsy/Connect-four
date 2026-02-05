import pygame as pg
from konstanter import *

class Rute:
    def __init__(self, rad, kol, str) -> None:
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
        pg.draw.circle(vindu, self.farge, (self.kol*100+50, VINDU_HOYDE-self.rad*100-50), CELLE_STR)

class Brett:
    def __init__(self) -> None:
        self.ant_rad = 6
        self.ant_kol = 7
        self.celle_str = CELLE_STR
        
        self.brett = [[Rute(r, k, self.celle_str) for r in range(self.ant_rad)] for k in range(self.ant_kol)]
    
    def draw(self, vindu):
        for kol in range(self.ant_kol):
            for rad in range(self.ant_rad):
                self.brett[kol][rad].draw(vindu)
    
    def sjekkSeier(self, rute:Rute):
        antPåRad=0
        for s in range(-3,4): #sjekk skrå ned
            if rute.kol+s in range(0,7) and rute.rad-s in range(0,6):
                antPåRad=antPåRad+1 if self.brett[rute.kol+s][rute.rad-s] == rute.farge else 0
                if antPåRad>=4:
                    return True
        
        antPåRad=0
        for s in range(-3,4): #sjekk skrå opp
            if rute.kol+s in range(0,7) and rute.rad+s in range(0,6):
                antPåRad=antPåRad+1 if self.brett[rute.kol+s][rute.rad+s] == rute.farge else 0
                if antPåRad>=4:
                    return True    
        antPåRad=0
        for s in range(-3,4): #sjekk horisontal
            if rute.kol+s in range(0,7):
                antPåRad=antPåRad+1 if self.brett[rute.kol+s][rute.rad] == rute.farge else 0 
                if antPåRad>=4:
                    return True    
        antPåRad=0
        if rute.rad-3>=0: #sjekk horisontal
            for s in range(4):
                antPåRad+=1 if self.brett[rute.kol][rute.rad-s] == rute.farge else 0
                if antPåRad>=4:
                    return True


        antPåRad=0
        for s in range(7): #sjekk skrå opp
            pass

        antPåRad=0
        for s in range(7): #sjekk horisontalt
            pass
        #sjekk ned
        
                
def hover(brett):
    mx2, my2 = pg.mouse.get_pos()
        
    for r in brett.brett[mx2//100]:
        if r.farge == WHITE or r.hover:
            r.hover = True
            break
        
    for i, k in enumerate(brett.brett):
        if i != mx2//100:
            for r in k:
                    r.hover = False