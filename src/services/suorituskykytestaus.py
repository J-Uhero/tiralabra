from random import randint
from services.a_star import A_star
from services.algortimi import Algoritmi
from services.heuristiikka import Heuristiikka
from services.heuristiikkafunktio import Heuristiikkafunktio as hf
from services.jps import JPS
from services.analysoi import Analysoi
from services.kuva import Kuva
from services.talletus import vakio_talletus as talletus
import time
from services.kuvaaja import Kuvaaja

class Suorituskykytestaus:
    def __init__(self, kuva: Kuva, matriisi):
        self.kuva = kuva
        self.matriisi = matriisi
        self.jps = JPS()
        self.a_star = A_star()
        self.leveys, self.korkeus = self.kuva.kuvan_koko()
    
    def hae_alku_ja_loppu(self, leveys, korkeus):
        x1 = x2 = y1 = y2 = 0
        while True:
            x1 = randint(1, leveys)
            y1 = randint(1, korkeus)
            if not self.matriisi[y1][x1]:
                break
        while True:
            x2 = randint(1, leveys)
            y2 = randint(1, korkeus)
            if self.matriisi[y2][x2]:
                continue
            elif (x1 == x2 and y1 == y2):
                continue
            else:
                break 
        return (x1,y1), (x2,y2)
    
    def testaa_algoritmeja(self, kierroksia):
        rivit = []
        t = time.time()
        for i in range(1,kierroksia+1):
    
            mista, minne = self.hae_alku_ja_loppu(self.leveys-1, self.korkeus-1)
            print("kierros:", i, "aika:", time.time()-t, "pisteet/este:", mista,"/"\
                  self.matriisi[mista[1]][mista[0]],",", minne,"/" self.matriisi[minne[1]][minne[0]]) 
            aloitus = time.time()
            _, edeltajat, pituus = self.a_star.aloita(mista, minne,
                                                      self.matriisi,
                                                      hf.pythagoras)
            lopetus = time.time()
            if edeltajat != None:
                rivit.append(talletus.palauta_rivi(Algoritmi.A_STAR, Heuristiikka.PYTHAGORAS,
                                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))

            aloitus = time.time()
            _, edeltajat, pituus = self.jps.aloita(mista, minne,
                                                   self.matriisi,
                                                   hf.pythagoras)
            lopetus = time.time()
            if edeltajat != None:
                rivit.append(talletus.palauta_rivi(Algoritmi.JPS, Heuristiikka.PYTHAGORAS, 
                                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))

            _, edeltajat, pituus = self.a_star.aloita(mista, minne,
                                                      self.matriisi,
                                                      hf.esteeton)
            lopetus = time.time()
            if edeltajat != None:
                rivit.append(talletus.palauta_rivi(Algoritmi.A_STAR, Heuristiikka.ESTEETON,
                                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))

            aloitus = time.time()
            _, edeltajat, pituus = self.jps.aloita(mista, minne,
                                                   self.matriisi,
                                                   hf.esteeton)
            lopetus = time.time()
            if edeltajat != None:
                rivit.append(talletus.palauta_rivi(Algoritmi.JPS, Heuristiikka.ESTEETON, 
                                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))
        talletus.talleta_lista(self.kuva.anna_tiedostonimi(), rivit)

def suorituskykytestaus_main():
    k = Kuva()
    s = Suorituskykytestaus(k)
    #s.testaa_algoritmeja(100)
    ku = Kuvaaja()
    ku.luo_algoritmien_aikavertailu(k.anna_tiedostonimi(), Heuristiikka.ESTEETON)
    ku.luo_algoritmien_aikavertailu(k.anna_tiedostonimi(), Heuristiikka.PYTHAGORAS)
    ku.luo_heuristiikan_aikavertailu(k.anna_tiedostonimi(), Algoritmi.A_STAR)
    ku.luo_heuristiikan_aikavertailu(k.anna_tiedostonimi(), Algoritmi.JPS)
    ku.luo_heuristiikkojen_solmuvertailu(k.anna_tiedostonimi(), Algoritmi.A_STAR)
    ku.luo_heuristiikkojen_solmuvertailu(k.anna_tiedostonimi(), Algoritmi.JPS)

    """
    ongelmia näiden kanssa (muttei liene enää):
    kierros: 8 aika 22.87881112098694 pisteet: (60, 105) False (1006, 847) False
    kierros: 16 aika 59.4746618270874 pisteet: (765, 550) False (894, 899) False
    kierros: 277 aika 1326.090215921402 pisteet: (293, 900) False (1066, 497) False

    kierros: 82 aika 373.6925950050354 pisteet: (1061, 513) False (240, 598) False
    """