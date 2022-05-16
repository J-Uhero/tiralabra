from random import randint
from entities.kuva import Kuva
# pylint: disable=invalid-name

class Matriisi:
    """Luokka kuvan analysointia varten ja sen muuttamiseksi matriisiksi,
    josta algoritmi voi tarkistaa mahdolliset seuraajasolmut.
    """

    def __init__(self, kuva: Kuva):
        self.kuva = kuva
        self.leveys, self.korkeus = self.kuva.kuvan_koko()
        self.matriisi = self.alusta(0)

    def alusta(self, arvo):
        """Alustaa solmuja ja esteitä kuvaavan matriisin

        Args:
            arvo (int): Kokonaisluku, joka kuvaa karttakuvan esteväriä (0 on musta)

        Returns:
            list: palauttaa kaksiulotteisen listan eli matriisin
        """
        m = []
        for y in range(self.korkeus):
            m.append([False]*self.leveys)
            for x in range(self.leveys):
                if self.kuva.vertaa_arvoa((x,y), arvo):
                    m[y][x] = True
        return m

    def anna_matriisi(self):
        return self.matriisi

    def arvo(self, koord):
        """Palauttaa matriisin arvon tietyssä koordinaatissa

        Args:
            koord (tuple): (x,y)

        Returns:
            boolen: totuusarvo matriisissa eli onko koordinaatissa estettä
        """
        if self.koordinaatti_matriisissa(koord):
            return self.matriisi[koord[0]][koord[1]]
        return False

    def koordinaatti_matriisissa(self, koord):
        """Tarkastaa, että koordinaatti on matriisin sisällä

        Args:
            koord (tupe): (x,y)

        Returns:
            boolean: totuusarvo, onko koordinaatti matriisissa
        """
        return 0 <= koord[0] and koord[0] < self.leveys and \
               0 <= koord[1] and koord[1] < self.korkeus

    def anna_satunnaiset_pisteet(self):
        """Palauttaa satunnaiset alku- ja loppupisteet matriisista,
        jotka eivät osu esteeseen

        Returns:
            tuple: (x,y), (x,y)
        """
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
