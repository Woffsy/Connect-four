import pygame as pg 
from konstanter import *
from brett import *

class Bot:
    def __init__(self,spiller,brett:Brett):
        self.spiller=spiller
        self.brett=brett
    


    


    def sjekkMuligSeier(self,spiller):
        for kol in self.brett.brett:
            SeierIKolonne=self.sjekkSeierTrekk(self.brett.brett,kol,spiller)
            if SeierIKolonne:
                return self.brett.brett.index(kol)
        return False
            
        
    def sjekkSeierTrekk(self,brett,kol,spiller):
        for rute in brett.brett[kol]:
            if r.farge == HOVER_FARGE or r.farge == WHITE:
                for r in RETTNINGER:
                    antPåRad=0
                    for s in range(-3,4):
                        if rute.kol+s*r[0] in range(0,7) and rute.rad+s*r[1] in range(0,6):
                            if s == 0:
                                antPåRad+=1
                            else:
                                antPåRad=antPåRad+1 if self.brett[rute.kol+s*r[0]][rute.rad+s*r[1]].farge == SPILLER_FARGER[spiller].farge else 0
                            if antPåRad>=4:
                                return True
                return False       
                               
                        

                        
                        
        
        
    
