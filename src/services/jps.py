from audioop import reverse
from heapq import heappop,heappush
import math
import time


SIJAINNIT = []
ESTEET = []
LOYDETYT = []

class JPS:
    """luokka JPS-algoritmille. Vaatii siistimistä debuggauksen jäljiltä ja hiomista.
    löytää tällä hetkellä vain jump pointit, muttei palauta käännöskohtia diagonaalihausta
    vaaka- ja pystyhauksi, mikäli niistä löytyy jump point.
    """

    def h_arvot(self, mista, minne):
        return math.sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)
    
    def sijainnit(self, leveys, korkeus):
        for i in range(korkeus):
            SIJAINNIT.append([0]*leveys)
    
    
    def tee_oikea_reitti(self, vanhemmat, loppu):
        reitti = [loppu]
        seuraaja = loppu
        kulmasolmu = None
        while seuraaja in vanhemmat.keys():
            vanhempi = vanhemmat[seuraaja]
            x_e = seuraaja[0]-vanhempi[0]
            y_e = seuraaja[1]-vanhempi[1]
            if abs(x_e) == abs(y_e) or \
                seuraaja[0] == vanhempi[0] or seuraaja[1] == vanhempi[1]:
                reitti.append(vanhempi)
                seuraaja = vanhempi
            else:
                if abs(x_e) > abs(y_e):
                    if y_e < 0:
                        y_e = -1 * y_e
                    kulmasolmu = (vanhempi[0]+y_e, seuraaja[1])
                else:
                    if x_e < 0:
                        x_e = -1 * x_e
                    kulmasolmu = (seuraaja[0], vanhempi[1]+x_e)
                reitti.append(kulmasolmu)
                reitti.append(vanhempi)
                seuraaja = vanhempi
        reitti.reverse()
        return reitti



    def aloita(self, alku, loppu, matriisi):
        t = time.time()
        if matriisi[alku[1]][alku[0]] or matriisi[loppu[1]][loppu[0]]:
            return -1, -1

        keko = [] # h_arvo, sijainti
        leveys = len(matriisi[0])
        korkeus = len(matriisi)
        edeltajat = {}
        vanhemmat = {}
        loydetyt = {}
        suunnat = {}
        suunnat[alku] = [(1,-1), (1,0), (1,1), (0,1),
                         (-1,1), (-1,0), (-1,-1), (0,-1)]
        g = {}
        self.sijainnit(leveys, korkeus)

        heappush(keko, (self.h_arvot(alku,loppu), alku))
        g[alku] = 0

        while len(keko) > 0:

            nykyinen = heappop(keko)

            if nykyinen[1] == loppu:
                return self.tee_oikea_reitti(vanhemmat, loppu), g[loppu]

            solmut = []
            for suunta in suunnat[nykyinen[1]]:
                solmut += self.haku(nykyinen[1],
                                        suunta,
                                        matriisi,
                                        leveys,
                                        korkeus,
                                        loppu,
                                        suunnat,
                                        t,
                                        edeltajat)

            for solmu in solmut:
                mahd_g = g[nykyinen[1]] + self.pisteiden_etaisyys(nykyinen[1], solmu)

                if solmu not in loydetyt.keys():
                    g[solmu] = math.inf
                    loydetyt[solmu] = True

                if mahd_g < g[solmu]:
                    g[solmu] = mahd_g

                    f_arvo = mahd_g + self.h_arvot(solmu, loppu)
                    heappush(keko, (f_arvo, solmu))
                    vanhemmat[solmu] = nykyinen[1]
    
    def matriisilla(self, x, y, matriisi):
        if x > len(matriisi[0]) or y > len(matriisi) or x < 0 or y < 0:
            return True
    
    def suunnan_sijoitus(self, solmu, suunta, suunnat):
        if solmu not in suunnat.keys():
            suunnat[solmu] = [suunta]
        else:
            if suunta not in suunnat[solmu]:
                suunnat[solmu].append(suunta)


    def haku(self, solmu, suunta, matriisi, leveys, korkeus, loppu, suunnat, t, vanhemmat):
        x, y = solmu
        alku = (x, y)
        pisteet = []

        while True:

            x1, y1 = x + suunta[0], y + suunta[1]
            x2, y2 = x1 + suunta[0], y1 + suunta[1]
            
            if x1 >= leveys or y1 >= korkeus or x1 < 0 or y1 < 0:
                return pisteet
                # haku mennyt yli kartan rajoista, jolloin palautetaan
                # löydetyt jump pointit

            if x1 == loppu[0] and y1 == loppu[1]:
                pisteet.append((x1,y1))
                self.suunnan_sijoitus((x1,y1), (0,0), suunnat)
                return pisteet
                # haku löysi maalisolmun, jolloin palautetaan löydetyt jump-pointit
                # ja maalisolmu§    
            
            if matriisi[y1][x1]:
                ESTEET.append((x1,y1))
                return pisteet
                #haku törmännyt esteeseen, jolloin ei voi edeteä.

            if suunta[0] == 0:
                #print("suunta x=0", x1, y1)
                if (0 <= y2 and suunta[1] == -1) or (y2 < korkeus and suunta[1] == 1):
                    #print("suunta x=0 ehto", x1, y1, suunta)
                # tarkastetaan, ettei olla ylimmällä riillä, jos suunta on ylös (-1) tai
                # alimmalla rivillä, jos suunta alas (1)

                    if x1 > 0 and matriisi[y1][x1-1] and not matriisi[y2][x1-1]:
                        pisteet.append((x1,y1))
                        self.suunnan_sijoitus((x1,y1), (-1, suunta[1]), suunnat)

                    if x1 <= leveys and matriisi[y1][x1+1] and not matriisi[y2][x1+1]:
                        pisteet.append((x1,y1))
                        self.suunnan_sijoitus((x1,y1), (1, suunta[1]), suunnat)


            elif suunta[1] == 0:
                if (0 <= x2 and suunta[0] == -1) or (x2 < leveys and suunta[0] == 1):
                # tarkastetaan, ettei olla vasemmanpuoleisemmalla riillä, jos suunta on vasen (-1) tai
                # oikeampuoleisimmalla rivillä, jos suunta oikea (1)

                    if y1 > 0 and matriisi[y1-1][x1] and not matriisi[y1-1][x2]:
                        #ylhäällä tilaa ja täyttyykö jp:n ehdot
                        pisteet.append((x1,y1))
                        self.suunnan_sijoitus((x1,y1), (suunta[0], -1), suunnat)

                    if y1+1 < korkeus and matriisi[y1+1][x1] == 1 and matriisi[y1+1][x2] == 0:
                        #alhaalla tilaa ja täyttyykö jp:n ehdot
                        pisteet.append((x1,y1))
                        self.suunnan_sijoitus((x1,y1), (suunta[0], 1), suunnat)


            else:
                #diagonaalihaku
                if matriisi[y1][x] and not matriisi[y][x1] and 0 <= y2 and y2 < korkeus:
                    if not matriisi[y2][x]:
                        pisteet.append((x1,y1))
                        vanhemmat[(alku)] = (x1,y2)
                        self.suunnan_sijoitus((x1,y1), (suunta[0]*(-1), suunta[1]), suunnat)
                
                if matriisi[y][x1] and not matriisi[y1][x] and 0 <= x2 and x2 < leveys:
                    if not matriisi[y][x2]:
                        pisteet.append((x1,y1))
                        vanhemmat[(alku)] = (x1,y2)
                        self.suunnan_sijoitus((x1,y1), (suunta[0], suunta[1]*(-1)), suunnat)
            
            if suunta[0] != 0 and suunta[1] != 0:
                loydetyt = []
                loydetyt += self.haku((x1,y1), (suunta[0],0), matriisi, leveys, korkeus, loppu, suunnat,t,vanhemmat)
                    # vaakahaku: jos diagonaalisuunta on ylä- tai alaviistoon oikealle,
                    # vaakahaku etenee myös oikealle ja päinvastoin

                loydetyt += self.haku((x1,y1), (0,suunta[1]), matriisi, leveys, korkeus, loppu, suunnat,t,vanhemmat)
                    # pystyhaku: jos diagonaalihaku etenee yläviistoon oikealle tai vasemmalle,
                    # pystyhaku etenee ylös ja päinvastoin

                    # pysty- ja vaakahaut palauttavat listat löydetyistä jump pointeista
                if len(loydetyt) > 0:
                    for p in loydetyt:
                        pisteet.append(p)
                        vanhemmat[(x1,y1)] = p
                        vanhemmat[(alku)] = (x1,y2)
            
            x += suunta[0]
            y += suunta[1]
                # tehdään lisäykset x- ja y-koordinaatteihin, jotta haku etenee
                # oikeaan suuntaan


    def pisteiden_etaisyys(self, vanhempi, piste):
        x_e = abs(vanhempi[0] - piste[0])
        y_e = abs(vanhempi[1] - piste[1])
        return abs(x_e - y_e) + math.sqrt(2) * min(x_e, y_e)

    