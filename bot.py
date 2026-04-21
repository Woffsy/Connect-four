from __future__ import annotations
import pygame as pg 
from konstanter import *
from brett import *
from spill import *
pg.init()

class Bot:
    def __init__(self,brett:Brett, spill:Spill):
        self.spiller=spill.botSinTur if spill.botSinTur else ""
        self.brett=brett
        self.spill=spill
    
    def botTrekk(self):
        kol=self.bestemBotTrekk()
        self.spill.plasserBrikke(kol)
        

    def bestemBotTrekk(self):
        if self.spiller=="Spiller 1":
            motspiller="Spiller 2"
        else:
            motspiller="Spiller 1"
        
        seierKol=self.sjekkMuligSeier(self.spiller)
        print(f"seierKol: {seierKol}")
        if seierKol != "False": #False = 0 så når seierKol var i kolonne 0 så kjører ikke returnen
            return seierKol
        
        motSeierKol=self.sjekkMuligSeier(motspiller)
        print(f"motSeierKol: {motSeierKol}")
        if motSeierKol != "False": #False = 0 så når motSeierKol var i kolonne 0 så kjører ikke returnen
            return motSeierKol
        




        #last resort
        for kol in BOTKOLPRIO:
            if self.brett.brett[kol][5].farge == WHITE or self.brett.brett[kol][5].farge == HOVER_FARGE:
                return kol
                
    def sjekkMuligSeier(self,spiller:str):
        for kol in self.brett.brett:
            SeierIKolonne=self.sjekkSeierTrekk(kol,spiller)
            if SeierIKolonne:
                return self.brett.brett.index(kol)
        return "False"
            
        
    def sjekkSeierTrekk(self,kol:list[Rute],spiller:str):
        for rute in kol:
            if rute.farge == HOVER_FARGE or rute.farge == WHITE:
                for r in RETTNINGER:
                    antPåRad=0
                    for s in range(-3,4):
                        if rute.kol+s*r[0] in range(0,7) and rute.rad+s*r[1] in range(0,6):
                            if s == 0:
                                antPåRad+=1
                            else:
                                antPåRad=antPåRad+1 if self.brett.brett[rute.kol+s*r[0]][rute.rad+s*r[1]].farge == SPILLER_FARGER[spiller] else 0
                            if antPåRad>=4:
                                return True
                return False       
    
    def sjekkTapTrekk(self):
        pass
                        

                        
                        
        
        
    
