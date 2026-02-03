import pygame as pg
from konstanter import *

class Rute:
    def __init__(self, rad, kol, str) -> None:
        self.rad = rad
        self.kol = kol
        self.str = str
        self.farge: tuple = WHITE
        
    def draw(self, vindu):
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