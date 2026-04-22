from __future__ import annotations
import pygame as pg 
from konstanter import *
from brett import *
from spill import *
from random import choice
pg.init()

class Bot:
    def __init__(self,brett:Brett, spill:Spill):
        self.spiller=spill.botSinTur if spill.botSinTur else ""
        self.motspiller="Spiller 2" if self.spiller=="Spiller 1" else "Spiller 1"
        self.brett=brett
        self.spill=spill
        self.muligeTrekk=[]

    def botTrekk(self):
        kol=self.bestemBotTrekk()
        self.spill.plasserBrikke(kol)
        

    def bestemBotTrekk(self):
        self.muligeTrekk=[]
        for kol in BOTKOLPRIO:
                if self.brett.brett[kol][5].farge == WHITE or self.brett.brett[kol][5].farge == HOVER_FARGE:
                    self.muligeTrekk.append(kol)
        
        seierKol=self.sjekkMuligSeier(self.spiller)
        if seierKol != "False": #False = 0 så når seierKol var i kolonne 0 så kjører ikke returnen
            return seierKol
        
        motSeierKol=self.sjekkMuligSeier(self.motspiller)
        if motSeierKol != "False": #False = 0 så når motSeierKol var i kolonne 0 så kjører ikke returnen
            return motSeierKol
        
        self.fjernTapendeTrekk(self.spiller)

        #har tapt
        if len(self.muligeTrekk)==0:
            for kol in BOTKOLPRIO:
                if self.brett.brett[kol][5].farge == WHITE or self.brett.brett[kol][5].farge == HOVER_FARGE:
                    return kol
        
        #last resort
        return choice(self.muligeTrekk)
        
        

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
    
    def fjernTapendeTrekk(self,spiller:str):
        kolNummer=0
        for kol in self.brett.brett:
            if self.sjekkTapendeTrekk(kol,spiller):
                self.muligeTrekk[:] = [x for x in self.muligeTrekk if x != kolNummer]
            kolNummer+=1
            

    def sjekkTapendeTrekk(self,kol:list[Rute],spiller:str):
        ruteNummer=0
        for rute in kol:
            ruteNummer+=1
            if (rute.farge == HOVER_FARGE or rute.farge == WHITE) and ruteNummer<6:
                for r in RETTNINGER:
                    antPåRad=0
                    for s in range(-3,4):
                        if rute.kol+s*r[0] in range(0,7) and ruteNummer+s*r[1] in range(0,6):
                            if s == 0:
                                antPåRad+=1
                            else:
                                antPåRad=antPåRad+1 if self.brett.brett[rute.kol+s*r[0]][ruteNummer+s*r[1]].farge == SPILLER_FARGER[self.motspiller] else 0
                            if antPåRad>=4:
                                return True
                return False             

                        
                        
        
        
    
