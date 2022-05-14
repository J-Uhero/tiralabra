from services.kuva import Kuva
from random import randint

class Analysoi:
    """Luokka kuvan analysointia varten ja muuttamista matriisiksi,
    josta algoritmi voi tarkistaa mahdolliset seuraajasolmut. Tarkastuksen
    voisi mahdollisesti tehdä myös suoraan kuvasta, mutta tämä ratkaisu lienee
    hivenen nopeampi reitin etsintävaiheessa. 
    """

    def __init__(self, kuva: Kuva):
        self.kuva = kuva
        self.leveys, self.korkeus = self.kuva.kuvan_koko()
        self.matriisi = self.alusta(0)
        self.np_matriisi = None
    
    def alusta(self, arvo):
        m = []
        for y in range(self.korkeus):
            m.append([False]*self.leveys)
            for x in range(self.leveys):
                if self.kuva.vertaa_arvoa((x,y), arvo):
                    m[y][x] = True
        return m
    
    def alusta_np_matriisi(self):
        self.np_matriisi = self.kuva.luo_np_taulukko()
    
    def alusta_matriisi(self):
        self.matriisi = self.aseta_arvot(0)
    
    def aseta_arvot(self, arvo):
        m = []
        for y in range(self.korkeus):
            m.append([])
            for x in range(self.leveys):
                m[y].append(self.kuva.vertaa_arvoa((x,y), arvo))
        return m

    def anna_matriisi(self):
        return self.matriisi
    
    def arvo(self, koord):
        if self.koordinaatti_matriisissa(koord):
            return self.matriisi[koord[0]][koord[1]]
        return False
    
    def koordinaatti_matriisissa(self, koord):
        return 0 <= koord[0] and koord[0] < self.leveys and \
               0 <= koord[1] and koord[1] < self.korkeus
    
    def anna_satunnaiset_pisteet(self):
        x1 = x2 = y1 = y2 = 0
        while True:
            x1 = randint(0, self.leveys-1)
            y1 = randint(0, self.korkeus-1)
            if not self.matriisi[y1][x1]:
                break
        while True:
            x2 = randint(0, self.leveys-1)
            y2 = randint(0, self.korkeus-1)
            if self.matriisi[y2][x2]:
                continue
            elif (x1 == x2 and y1 == y2):
                continue
            else:
                return (x1, y1), (x2, y2)
    
    def np_arvo(self, koord):
        return self.np_matriisi[koord[0]][koord[1]]

    def tulosta_matriisi(self):
        print(self.matriisi)

#vakio_analysoi = Analysoi(Kuva())
