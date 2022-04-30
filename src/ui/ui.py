from services.a_star import A_star
from services.jps import JPS
from services.analysoi import Analysoi
from services.kuva import Kuva
import time

class Ui:
    """Ohjelman käyttöliittymä. Käyttöliittymä kehittynee kurssin edetessä.
    Vaikka kerkesin jo hieman tutkia Pillow-kirjastoa ja suunnitella kartta-
    reittien piirtämistä, ajattelin kuitenkin tehdä aluksi pelkästään komento-
    riviltä suoritettavan ja ASCII-visualisoidun käyttöliittymän.
    """

    def __init__(self):

        self.m1 = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0]
            ]

        self.m2 = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0]
            ]

    def aloita(self):
        """funktio, joka aloittaa käyttöliittymän ja ohjelman toiminnan
        """
        """
        teksti = "\nOhjelma tällä hetkellä demonstroi A*-algoritmin toimintaa " \
                 "tulostamalla kaksi eri matriisikarttaa. Kummankin kartan kohdalla " \
                 "ensin tulostetaan " \
                 "kartta ilman reittiä ja sen jälkeen algoritmin etsimä lyhin " \
                 "pisteiden (0,0) ja (4,3) välillä etsitty reitti samassa kartassa. " \
                 "Kyseiset pisteet ovat karttojen vasen yläkulma ja oikea alakulma. " \
                 "Kartassa 0 kuvaa pistettä, jossa voi liikkua, 1 kuvaa estettä ja 2 " \
                 "Algoritmin hakemaa reittiä.\n"

        print(teksti, "\nkartta 1:\n")
        #self.tulosta_matriisi(self.m1)
        print("\nreitin kanssa:\n")
        #self.tulosta_matriisi(self.luo_reittimatriisi(self.m1, a_star((0,0), (4,3), m=self.m1)))
        print("\nkartta 2:\n")
        #self.tulosta_matriisi(self.m2)
        print("\nreitin kanss:a\n")
        #self.tulosta_matriisi(self.luo_reittimatriisi(self.m2, a_star((0,0), (4,3), m=self.m2)))
        print("\n")

        """

        kuva = Kuva()
        m2 = Analysoi(kuva)
        jps = JPS()
        t = time.time()
        solmut, matka = jps.aloita((10,10), (1050,200), m2.anna_matriisi())
        print("jps aika:", time.time()-t, "matka:", matka)
        kuva.piirra_vareissa(solmut)
        kuva.nayta_vareissa()

        kuva = Kuva()
        a_star = A_star()
        t = time.time()
        solmut2, matka2 = a_star((10,10), (1050,200), m2.anna_matriisi())
        print("a_star, aika:", time.time()-t, "matka:", matka2)
        kuva.piirra_vareissa(solmut2)
        kuva.nayta_vareissa()


    def silmukka(self):
        pass

    def luo_reittimatriisi(self, m, reitti):
        """funktio uuden matriisin, jossa reitti näkyy, luomista varten
        """
        uusi_m = list(m)
        for k in reitti:
            uusi_m[k[1]][k[0]] = 2
        return uusi_m

    def tulosta_matriisi(self, m):
        """funktio matriisin tulostamiseen
        """
        for i in range(len(m)):
            print(m[i])

vakio_ui = Ui()
