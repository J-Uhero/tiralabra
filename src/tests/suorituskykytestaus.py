import time
from services.a_star import A_star
from enums.algortimi import Algoritmi
from enums.heuristiikka import Heuristiikka
from services.heuristiikkafunktio import Heuristiikkafunktio as hf
from services.jps import JPS
from entities.matriisi import Matriisi
from entities.kuva import Kuva
from repository.talletus import vakio_talletus as talletus

class Suorituskykytestaus:
    """Luokka, joka ajaa algoritmeja lukuisia kertoja satunnaisilla alku- ja
    päätöspisteillä suorituskyvyn testaamista varten
    """
    def __init__(self, kuva: Kuva, matriisi: Matriisi):
        self.kuva = kuva
        self.matriisi = matriisi
        self.m = matriisi.anna_matriisi()
        self.jps = JPS()
        self.a_star = A_star()
        self.leveys, self.korkeus = self.kuva.kuvan_koko()

    def testaa_algoritmeja(self, kierroksia):
        """Funktio, joka käynnistää testaamisen

        Args:
            kierroksia (int): luku, joka kertoo testausten määrän
        """
        rivit = []
        t = time.time()
        for i in range(1,kierroksia+1):

            mista, minne = self.matriisi.anna_satunnaiset_pisteet()
            aloitus = time.time()
            _, edeltajat, pituus = self.a_star.aloita(mista, minne, self.m, hf.pythagoras)
            lopetus = time.time()
            if edeltajat is not None:
                rivit.append(talletus.palauta_rivi(Algoritmi.A_STAR, Heuristiikka.PYTHAGORAS,
                                    mista, minne, pituus, lopetus-aloitus, len(edeltajat)))
            pituus1 = "{:.2f}".format(pituus)

            aloitus = time.time()
            _, edeltajat, pituus = self.jps.aloita(mista, minne, self.m, hf.pythagoras)
            lopetus = time.time()
            if edeltajat is not None:
                rivit.append(talletus.palauta_rivi(Algoritmi.JPS, Heuristiikka.PYTHAGORAS,
                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))
            pituus2 = "{:.2f}".format(pituus)

            _, edeltajat, pituus = self.a_star.aloita(mista, minne, self.m, hf.esteeton)
            lopetus = time.time()
            if edeltajat is not None:
                rivit.append(talletus.palauta_rivi(Algoritmi.A_STAR, Heuristiikka.ESTEETON,
                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))
            pituus3 = "{:.2f}".format(pituus)

            aloitus = time.time()
            _, edeltajat, pituus = self.jps.aloita(mista, minne, self.m, hf.esteeton)
            lopetus = time.time()
            if edeltajat is not None:
                rivit.append(talletus.palauta_rivi(Algoritmi.JPS, Heuristiikka.ESTEETON,
                                mista, minne, pituus, lopetus-aloitus, len(edeltajat)))
            pituus4 = "{:.2f}".format(pituus)
            
            print(f"kierros: {i}, aika: {time.time()-t:.2f}, pisteet/este: {mista}/"+\
                  f"{self.m[mista[1]][mista[0]]} {minne}/{self.m[minne[1]][minne[0]]},"+\
                  f" samat pituudet: {pituus1 == pituus2 == pituus3 == pituus4}")
            
        talletus.talleta_lista(self.kuva.anna_tiedostonimi(), rivit)
    
