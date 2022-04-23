from heapq import heappop, heappush

class Solmu:
    
    def __init__(self, sijainti, suunta=None, vanhempi=None):
        self._sijainti = sijainti # (x, y)
        self._suunta = suunta # (1/-1, 1/-1)
        self._vanhempi = vanhempi # (x, y)
    
    def liiku(self):
        self._sijainti = (self._sijainti[0]+self._suunta[0],
                          self._sijainti[1]+self._suunta[1])

    @property
    def sijainti(self):
        return self._sijainti
    
    @sijainti.setter
    def sijainti(self, koord):
        self._sijainti = koord
    
    @property
    def suunta(self):
        return self._suunta
    
    @suunta.setter
    def suunta(self, koord):
        self._suunta = koord
    
    @property
    def vanhempi(self):
        return self._vanhempi
    
    @vanhempi.setter
    def vanhempi(self, solmu):
        self._vanhempi = solmu


class Jps:

    def __init__(self, s, e, m):
        """luokka JPS-algoritmille

        Args:
            s (tuple): lähtösolmu muotoa (x,y)
            e (tuple): päämääräsolmu muotoa (x,y)
            m (list): verkkoa/karttaa kuvaava matriisi koostuen listoista listassa
        """

        self.s = s
        self.e = e
        self.m = m
        self.leveys = len(m[0])
        self.korkeus = len(m)
        self.jp = []

    def a_star(self):
        pass

    def aloita(self):
        pass

    def jump_point(self, s, e, m):
        for suunta in [(0,1), (1,0), (0,-1), (-1,0)]:
            self.pysty_vaaka_haku(s, m, suunta, e)
                # aluksi pysty- ja vaakahaut lähtöpisteestä tai jump pointista

        for suunta in [(1,-1), (1,1), (-1,1), (-1,-1)]:
            solmu = (s[0]+suunta[0], s[1]+suunta[1])
            self.diagonaali_haku(solmu, m, suunta, e)
                # sitten diagonaalihaut


    def diagonaali_tarkistus(self, solmu, suunta, vanhempi):
        # en tiedä tarvitaanko vai riittääkö pysty-/vaakatarkistus
        tarkistus1 = (solmu[0], solmu[1] + (-1) * suunta[1])
            # kohta samalla x-akselin kohdalla, josta tarkastetaan estettä
        tarkistus2 = (solmu[0] + (-1) * suunta[0], solmu[1])
            # kohta samalla y-akselin kohdalla

        if self.m[tarkistus1[0]][tarkistus1[1]] and not self.m[tarkistus2[0]][tarkistus2[1]]:
            # tarkastetaan onko estettä tarkistuskohdassa
            fn1 = (tarkistus1[0] + suunta[0], tarkistus1[0]) 
                # forced neighbour tarkistus1:n vieressä
            if not self.m[fn1[0]][fn1[1]]:
                # tarkastetaan ettei ole estettä
                heappush(self.jp, Solmu(solmu, suunta, vanhempi))
                    # lisätään solmu jump pointiksi

                    # HUOM! SUUNTA EI OIKEA. PITÄÄ TARKASTAA VIELÄ


        if not self.m[tarkistus1[0]][tarkistus1[1]] and self.m[tarkistus2[0]][tarkistus2[1]]:
            fn2 = (tarkistus2[0], tarkistus2[1] + suunta[1])
                # forced neighbour tarkistus2:n vieressä
            if not self.m[fn2[0]][fn2[1]]:
                # tarkastetaan ettei ole estettä
                heappush(self.jp, Solmu(solmu, suunta, vanhempi))
                    # lisätään solmu jump pointiksi


    def pysty_vaaka_tarkistus(self, koord, suunta, vanhempi):
        """Funktio, jossa tarkastetaan, onko tarvetta jump pointille,
           kun kuljetaan vaaka- tai pystysuunnassa.

        Args:
            koord (tuple): sijainti koordinaattina (x,y)
            suunta (tuple): kulkusuunta
            vanhempi (Solmu): vanhempisolmu
        """

        if suunta[0] == 0:
            # pystysuunta
            if (0 < koord[1] and suunta[1] == -1) or (koord[1] < self.korkeus and suunta[1] == 1):
                # tarkastetaan, ettei olla ylimmällä riillä, jos suunta on ylös (-1) tai
                # alimmalla rivillä, jos suunta alas (1)

                if koord[0] > 0 and self.m[koord[0]-1][koord[1]]:
                    # tarkastetaan ettei olla vasemmassa reunassa ja onko vasemmalla este
                    heappush(self.jp, Solmu(koord, (-1, suunta[1]), vanhempi))
                        # lisätään jump point. suuntana vasen ylä- tai alaviisto
  
                if koord[0] < self.leveys and self.m[koord[0]+1][koord[1]]:
                    # tarkastetaan, ettei olla oikeassa reunassa ja onko oikealla este
                    heappush(self.jp, Solmu(koord, (1, suunta[1]), vanhempi))
                        # lisätään jump point. suuntana oikea ylä- tai alaviisto
        
        if suunta[1] == 0:
            # vaakasuunta 
            if (0 < koord[0] and suunta[0] == -1) or (koord[0] < self.leveys and suunta[0] == 1): 
                # tarkastetaan, ettei olla vasemmassa laidassa, jos suunta vasemmalle tai
                # ettei olla oikeassa laidassa, jos suunta oikealle

                if koord[1] > 0 and self.m[koord[0]][koord[1]-1]:
                    # tarkastetaan ettei olla yläreunassa ja onko yläpuolella estettä
                    heappush(self.jp, Solmu(koord, (suunta[0], -1), vanhempi))
                        # lisätään jump point. suunta oikea- tai vasen yläviisto

                if koord[1] < self.korkeus and self.m[koord[0]][koord[1]+1]:
                    # tarkastetaan ettei olla alareunassa ja onko alapuolella estettä
                    heappush(self.jp, Solmu(koord, (suunta[0], 1), vanhempi))
                        # lisätään jump point. suunta oikea- tai vasen alaviisto


    def diagonaali_haku(self, s, m, suunta, e):
        """Kartta/matriisi tarkastetaan ja etsitään jump pointit eli hyppypisteet/-solmut.
        Etsiminen aloitetaan diagonaalilla haulla, josta käsin tehdään horisontaaliset
        ja vertikaaliset haut. Haku palauttaa löydetyt jump pointit ja maalisolmun, mikäli
        se löydetään haulla.

        Args:
            s (tuple): lähtösolmu muotoa (x,y)
            m (lista): karttaa ja solmuja kuvaava matriisi, joka koostuu listoista
                       listojen sisällä.
            suunta (tuple): suunta kertoo (x,y) muodossa lisäyksen (+1 tai -1 ) nykyiseen
                            solmuun, jotta haku etenee haluttuun suuntaan
            maali (tuple): maalisolmu muotoa (x,y)

        Returns:
            list: lista jump pointeista (ja löytyessään maalisolmusta)
        """

        x, y = s
        jp = []
        matka = 0
        while True:
            # diagonaalihaun pääsilmukka
            
            if  x > self.leveys or y > self.korkeus or x < 0 or y < 0:
                return jp
                # haku mennyt yli kartan rajoista, jolloin palautetaan
                # löydetyt jump pointit

            if x == e[0] and y == e[1]:
                return jp.append((x,y))
                # haku löysi maalisolmun, jolloin palautetaan löydetyt jump-pointit
                # ja maalisolmu§    
            
            if m[y][x] == 1:
                return jp
                #haku törmännyt esteeseen, jolloin ei voi edeteä.
            
            
            jp += self.pysty_vaaka_haku(s=(x,y), m=m, suunta=(suunta[0],0), e=e)
                # vaakahaku: jos diagonaalisuunta on ylä- tai alaviistoon oikealle,
                # vaakahaku etenee myös oikealle ja päinvastoin

            jp += self.pysty_vaaka_haku(s=(x,y), m=m, suunta=(0,suunta[1]), e=e)
                # pystyhaku: jos diagonaalihaku etenee yläviistoon oikealle tai vasemmalle,
                # pystyhaku etenee ylös ja päinvastoin

                # pysty- ja vaakahaut palauttavat listat löydetyistä jump pointeista, jotka
                # lisätään jp eli jump point -listaan
            
            x += suunta[0]
            y += suunta[1]
                # tehdään lisäykset x- ja y-koordinaatteihin, jotta haku etenee
                # diagonaalisesti oikeaan suuntaan

    
    def pysty_vaaka_haku(self, s, m, suunta, e):
        """tässä tarkistetaan matriisia pysty- tai vaakasuuntaisesti ja etsitään
        jump pointeja ja päämääräsolmua. funktio ajetaan diagonaalihaun sisällä

        Args:
            s (_type_): _description_
            m (_type_): _description_
            suunta (_type_): _description_
            e (_type_): _description_
        
        Palautus:
            list: lista löydetyistä jump point -solmuista
        """

        x, y = s
        jp = []
        este_oikealla = False
        este_vasemmalla = False

        while True:
            # vaaka- ja pystyhaun pääsilmukka
            
            x += suunta[0]
            y += suunta[1]
            # kuljetaan määriteltyyn suuntaan tekemällä lisäykset x- ja y-koordinaatteihin

            if  x > self.leveys or y > self.korkeus or x < 0 or y < 0:
                return jp
                # haku mennyt yli kartan rajoista, jolloin palautetaan
                # löydetyt jump pointit

            if x == e[0] and y == e[1]:
                return jp.append((x,y))
                # haku löysi maalisolmun, jolloin palautetaan löydetyt jump-pointit
                # ja maalisolmu
            
            if m[y][x] == 1:
                return jp
                #haku törmännyt esteeseen, jolloin ei voi edeteä.
            
            if suunta[0] == 0:
                # tarkistetaan, kuljetaanko pystysuunnassa
                if m[x+1][y] == 1:
                    este_oikealla = True
                elif m[x-1][y] == 1:
                    este_vasemmalla = True
                        # tarkistetaan, onko jommalla kummalla puolella este.

                if (este_oikealla and m[x+1][y] == 0) or (este_vasemmalla and m[x-1][y] == 0):
                    jp.append((x,y))
                    # tarkistetaan, onko vieressä ollut este ja onko se loppunut.
                    # silloin lisätään sijainti jump pointiksi jp-listaan

            if suunta[1] == 0:
                # tarkastetaan, kuljetaanko vaakasuunnassa
                if m[x][y+1] == 1:
                    este_oikealla = True
                elif m[x][y-1] == 1:
                    este_vasemmalla = True
                        # tarkistetaan, onko jommalla kummalla puolella este.

                if (este_oikealla and m[x][y+1] == 0) or (este_vasemmalla and m[x][y-1] == 0):
                    jp.append((x,y))
                        # tarkistetaan, onko vieressä ollut este ja onko se loppunut.
                        # silloin lisätään sijainti jump pointiksi jp-listaan

if __name__ == "__main__":
    solmu = Solmu((0,0), (1,0), "jee")
    solmu.sijainti = (1,1)
    print(solmu.sijainti)
    solmu.liiku()
    print(solmu.sijainti)