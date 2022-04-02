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
    
    def aloita(self):
        pass

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
        while True:
            # diagonaalihaun pääsilmukka
            
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
