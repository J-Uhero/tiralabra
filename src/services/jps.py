from heapq import heappop,heappush
import math
import time
SIJAINNIT = []
LISATYT = []

class JPS:
    """luokka JPS-algoritmille. Vaatii siistimistä debuggauksen jäljiltä ja hiomista.
    löytää tällä hetkellä vain jump pointit, muttei palauta käännöskohtia diagonaalihausta
    vaaka- ja pystyhauksi, mikäli niistä löytyy jump point.
    """

    def h_arvot(self, mista, minne):
        return math.sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)
    
    def tee_oikea_reitti(self, vanhemmat, loppu):
        reitti = [loppu]
        seuraaja = loppu
        while seuraaja in vanhemmat.keys():
            vanhempi = vanhemmat[seuraaja]
            if abs(seuraaja[0]-vanhempi[0]) == abs(seuraaja[1]-vanhempi[1]) or \
                seuraaja[0] == vanhempi[0] or seuraaja[1] == vanhempi[1]:
                reitti.append(vanhempi)
                seuraaja = vanhempi
            else:
                x_e = seuraaja[0]-vanhempi[0]
                y_e = seuraaja[1]-vanhempi[1]
                if abs(x_e) > abs(y_e):
                    edeltaja = ((vanhempi[0]),seuraaja[1])
                    pass


    def jps(self, alku, loppu, matriisi):

        keko = [] # h_arvo, sijainti
        leveys = len(matriisi[0])
        korkeus = len(matriisi)
        edeltajat = {}
        loydetyt = {}
        suunnat = {}
        suunnat[alku] = [(1,-1), (1,0), (1,1), (0,1),
                         (-1,1), (-1,0), (-1,-1), (0,-1)]
        g = {}

        heappush(keko, (self.h_arvot(alku,loppu), alku))
        g[alku] = 0

        while len(keko) > 0:
            nykyinen = heappop(keko)

            if nykyinen[1] == loppu:
                print("loppu")
                return edeltajat, g

            pisteet = []
            for suunta in suunnat[nykyinen[1]]:
                pisteet += self.haku(nykyinen[1],
                                        suunta,
                                        matriisi,
                                        leveys,
                                        korkeus,
                                        loppu,
                                        suunnat)
            #self.piirra(SIJAINNIT)
            #print(pisteet)

            for piste in pisteet:

                mahd_g = g[nykyinen[1]] + self.pisteiden_etaisyys(nykyinen[1], piste)
                #print(nykyinen[1], piste, mahd_g, g[nykyinen[1]], self.pisteiden_etaisyys(nykyinen[1], piste),self.h_arvot(piste, loppu))

                if piste not in loydetyt.keys():
                    g[piste] = math.inf

                if mahd_g < g[piste]:
                    g[piste] = mahd_g

                    f_arvo = mahd_g + self.h_arvot(piste, loppu)
                    #print("p", piste, "f", f_arvo)
                    #print("lisataan kekoon", piste, f_arvo, suunnat[piste])
                    heappush(keko, (f_arvo, piste))
                    edeltajat[piste] = nykyinen[1]
                    #print(edeltajat)
    
    def matriisilla(self, x, y, matriisi):
        if x > len(matriisi[0]) or y > len(matriisi) or x < 0 or y < 0:
            return True
    
    def suunnan_sijoitus(self, solmu, suunta, suunnat):
        if solmu not in suunnat.keys():
            suunnat[solmu] = []
        suunnat[solmu].append(suunta)
        #print("sijoitettu")


    def haku(self, solmu, suunta, matriisi, leveys, korkeus, loppu, suunnat):
        #print("uusi haku", solmu, suunta)
        x, y = solmu
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
                #print("suunta y=0", x1, y1, suunta)
                if (0 <= x2 and suunta[0] == -1) or (x2 < leveys and suunta[0] == 1):
                    #print("suunta y=0 ehto", x1, y1, suunta)
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
                        self.suunnan_sijoitus((x1,y1), (suunta[0]*(-1), suunta[1]), suunnat)
                        #print("diag piste", x1, y1, "v", suunta, "u", (suunta[0]*(-1), suunta[1]))
                
                if matriisi[y][x1] and not matriisi[y1][x] and 0 <= x2 and x2 < leveys:
                    if not matriisi[y][x2]:
                        pisteet.append((x1,y1))
                        self.suunnan_sijoitus((x1,y1), (suunta[0], suunta[1]*(-1)), suunnat)
                        #print("diag piste2", x1, y1, "v", suunta, "u", (suunta[0], suunta[1]*(-1)))
            
            if suunta[0] != 0 and suunta[1] != 0:
                pisteet += self.haku((x1,y1), (suunta[0],0), matriisi, leveys, korkeus, loppu, suunnat)
                    # vaakahaku: jos diagonaalisuunta on ylä- tai alaviistoon oikealle,
                    # vaakahaku etenee myös oikealle ja päinvastoin

                pisteet += self.haku((x1,y1), (0,suunta[1]), matriisi, leveys, korkeus, loppu, suunnat)
                    # pystyhaku: jos diagonaalihaku etenee yläviistoon oikealle tai vasemmalle,
                    # pystyhaku etenee ylös ja päinvastoin

                    # pysty- ja vaakahaut palauttavat listat löydetyistä jump pointeista, jotka
                    # lisätään jp eli jump point -listaan
            
            x += suunta[0]
            y += suunta[1]
                # tehdään lisäykset x- ja y-koordinaatteihin, jotta haku etenee
                # oikeaan suuntaan


    def pisteiden_etaisyys(self, vanhempi, piste):
        x_e = abs(vanhempi[0] - piste[0])
        y_e = abs(vanhempi[1] - piste[1])
        return abs(x_e - y_e) + math.sqrt(2) * min(x_e, y_e)
    
    def piirra(self, lista):
        m = []
        for i in range(4):
            m.append([0]*5)
        for l in lista:
            m[l[1]][l[0]] = 1
        for r in m:
            print(r)




if __name__ == "__main__":
    t = time.time()     
    m1 = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0]
            ]

    jps = JPS()
    print(jps.jps((0,0), (4,3), m1))
    print(time.time()-t)
    