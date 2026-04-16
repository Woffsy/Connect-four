import pygame as pg 
from konstanter import *
from brett import *
from spill import *
pg.init()

class Bot:
    def __init__(self,spiller: str,brett:Brett, spill:Spill):
        self.spiller=spiller
        self.brett=brett
        self.spill=spill
    
   
    def botTrekk(self):
        if self.spiller=="Spiller 1":
            motspiller="Spiller 2"
        else:
            motspiller="Spiller 1"
        
        seierkol=self.sjekkMuligSeier(self.spiller)
        if seierkol != False:
            self.spill.plasserBrikke(self.spiller,seierkol)
        
        motSeierKol=self.sjekkMuligSeier(motspiller)
        if motSeierKol != False:
            self.spill.plasserBrikke(motspiller,motSeierKol)
        




        #last resort
        for kol in BOTKOLPRIO:
            if self.brett.brett[kol][5].farge == WHITE or self.brett.brett[kol][5].farge == HOVER_FARGE:
                self.spill.plasserBrikke(self.spiller,kol)
                
    def sjekkMuligSeier(self,spiller:str):
        for kol in self.brett.brett:
            SeierIKolonne=self.sjekkSeierTrekk(kol,spiller)
            if SeierIKolonne:
                return self.brett.brett.index(kol)
        return False
            
        
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
                        

                        
                        
        
        
    
