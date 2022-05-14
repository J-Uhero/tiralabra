from services.a_star import A_star
from services.algortimi import Algoritmi
from services.heuristiikka import Heuristiikka
from services.heuristiikkafunktio import Heuristiikkafunktio as hf
from services.jps import JPS
from services.analysoi import Analysoi
from services.kuva import Kuva
from services.suorituskykytestaus import Suorituskykytestaus
from services.kuvaaja import Kuvaaja
import time

OTSIKKO = "\nA*- ja JPS-algoritmien vertailu ja visualisointi"
PAAVALIKKO_VALINNAT = ["1: Aja algoritmi",
            "2: Vertaa algoritmeja",
            "3: Vertaa heuristiikkaa",
            "4: Asetukset",
            "5: Suorituskyky",
            "0: Lopeta"]
ASETUKSET_VALINNAT = ["1: Aseta algoritmi",
            "2: Aseta heuristiikka",
            "3: Aseta kuvatiedosto",
            "4: Aseta lähtö- ja päätepiste",
            "0: Palaa"]
VIRHE = "Virheellinen syöte"

class Ui:
    """Ohjelman käyttöliittymä. Käyttöliittymä kehittynee kurssin edetessä.
    Vaikka kerkesin jo hieman tutkia Pillow-kirjastoa ja suunnitella kartta-
    reittien piirtämistä, ajattelin kuitenkin tehdä aluksi pelkästään komento-
    riviltä suoritettavan ja ASCII-visualisoidun käyttöliittymän.
    """

    def __init__(self):
        self.kuva = Kuva()
        self.matriisi = Analysoi(self.kuva)
        self.algoritmi = Algoritmi.A_STAR
        self.heuristiikka = Heuristiikka.PYTHAGORAS
        self.lahtopiste = (10,10)
        self.paatospiste = (1050,200)

    def aloita(self):
        print(OTSIKKO)
        self.tulosta_asetukset()
        self.paavalikko()

    def tulosta_asetukset(self):
        asetukset = f"\nAlgoritmi: {self.algoritmi.value}, Heuristiikka: {self.heuristiikka.value}\n"\
                    f"Lähtö: {self.lahtopiste}, Päätös: {self.paatospiste}, "\
                    f"Karttakuva: {self.kuva.anna_tiedostonimi()}\n"
        print(asetukset)

    def paavalikko(self):
        while True:
            for valinta in PAAVALIKKO_VALINNAT:
                print(valinta)

            syote = input("> ")
            if syote == "0":
                break
            elif syote == "1":
                self.aja_algoritmi(self.algoritmi, self.heuristiikka)
            elif syote == "2":
                self.vertaa_algoritmeja()
            elif syote == "3":
                self.vertaa_heuristiikkaa()
            elif syote == "4":
                self.asetukset()
            elif syote == "5":
                self.suorituskyky()
            else:
                print(VIRHE)
            print("\n")

    def aja_algoritmi(self, algoritmi, heuristiikka):
        aloitus = lopetus = reitti = edeltajat = pituus = None
        if algoritmi == Algoritmi.A_STAR:
            a_star = A_star()
            aloitus = time.time()
            reitti, edeltajat, pituus = a_star.aloita(self.lahtopiste,
                                                      self.paatospiste,
                                                      self.matriisi.anna_matriisi(),
                                                      h=self.palauta_heuristiikkafunktio(heuristiikka))
            lopetus = time.time()

        if algoritmi == Algoritmi.JPS:
            jps = JPS()
            aloitus = time.time()
            reitti, edeltajat, pituus = jps.aloita(self.lahtopiste,
                                                   self.paatospiste,
                                                   self.matriisi.anna_matriisi(),
                                                   h=self.palauta_heuristiikkafunktio(heuristiikka))
            lopetus = time.time()

        if edeltajat != None:
            self.tulosta_algoritmin_tiedot(algoritmi, heuristiikka, pituus, lopetus-aloitus, len(edeltajat))
            if algoritmi == Algoritmi.A_STAR:
                self.kuva.tulosta_a_star(reitti, edeltajat)
            if algoritmi == Algoritmi.JPS:
                self.kuva.tulosta_jps(reitti, edeltajat)
        else:
            print("\nEi reittiä löydettävissä")

    def tulosta_algoritmin_tiedot(self, algoritmi, heuristiikka, pituus, aika, edeltajia):
        tulostus = f"\nAlgoritmi: {algoritmi.value}\nHeuristiikka: {heuristiikka.value}\n"\
                   f"Reitin pituus: {pituus}\nAika: {aika}\n"\
                   f"tutkittuja solmuja: {edeltajia}"
        print(tulostus)

    def palauta_heuristiikkafunktio(self, heuristiikka):
        if heuristiikka == Heuristiikka.PYTHAGORAS:
            return hf.pythagoras
        if heuristiikka == Heuristiikka.MANHATTAN:
            return hf.manhattan
        if heuristiikka == Heuristiikka.ESTEETON:
            return hf.esteeton

    def vertaa_algoritmeja(self):
        self.aja_algoritmi(Algoritmi.A_STAR, self.heuristiikka)
        self.aja_algoritmi(Algoritmi.JPS, self.heuristiikka)

    def vertaa_heuristiikkaa(self):
        self.aja_algoritmi(self.algoritmi, Heuristiikka.PYTHAGORAS)
        self.aja_algoritmi(self.algoritmi, Heuristiikka.ESTEETON)
        self.aja_algoritmi(self.algoritmi, Heuristiikka.MANHATTAN)

    def asetukset(self):
        while True:
            self.tulosta_asetukset()
            for valinta in ASETUKSET_VALINNAT:
                print(valinta)
            syote = input("> ")
            if syote == "0":
                break
            elif syote == "1":
                self.aseta_algoritmi()
            elif syote == "2":
                self.aseta_heuristiikka()
            elif syote == "3":
                self.aseta_kuva()
            elif syote == "4":
                self.aseta_hakukoordinaatit()
            else:
                print(VIRHE)

    def aseta_algoritmi(self):
        print("\nA*: 1\nJPS: 2\nPalaa: 0")
        syote = input("> ")
        if syote == "0":
            return
        elif syote == "1":
            self.algoritmi = Algoritmi.A_STAR
        elif syote == "2":
            self.algoritmi = Algoritmi.JPS
        else:
            print(VIRHE)

    def aseta_heuristiikka(self):
        print("\n1: Pythagoras\n2: Esteetön etäisyys\n3: Manhattan\n0: Palaa")
        syote = input("> ")
        if syote == "0":
            return
        elif syote == "1":
            self.heuristiikka = Heuristiikka.PYTHAGORAS
        elif syote == "2":
            self.heuristiikka = Heuristiikka.ESTEETON
        elif syote == "3":
            self.heuristiikka = Heuristiikka.MANHATTAN 
        else:
            print(VIRHE)

    def aseta_kuva(self):
        print("Anna kansiossa /src/data olevan kuvatiedoston nimi:")
        syote = input("> ")
        if self.kuva.lataa_kuva(syote):
            self.matriisi = Analysoi(self.kuva)
            print("\nKuvan lisäys onnistui!")
        else:
            print(f"\n Kuvatiedoston {syote} lisäys epäonnistui")

    def aseta_hakukoordinaatit(self):
        while True:
            print("\n1: Alkupiste\n2: Päätepiste\n3: Satunnaiset\n0: Palaa")
            syote = input("> ")
            if syote == "0":
                break
            elif syote == "1":
                self.aseta_lahtopiste()
            elif syote == "2":
                self.aseta_paatepiste()
            elif syote == "3":
                self.aseta_satunnaiset_pisteet()
            else:
                print(VIRHE)

    def aseta_lahtopiste(self):
        print("\nAnna lähtöpisteen koordinaatit")
        esteeton, koord = self.kysy_koordinaatit()
        if esteeton is None:
            return
        elif esteeton:
            print("Epäkelpo koordinaatti")
        else:
            self.lahtopiste = koord
            print("Lähtöpisteen lisäys onnistui!")

    def aseta_paatepiste(self):
        print("\nAnna päätepisteen koordinaatit")
        esteeton, koord = self.kysy_koordinaatit()
        if esteeton is None:
            return
        elif esteeton:
            print("Epäkelpo koordinaatti")
        else:
            self.paatospiste = koord
            print("Päätepisteen lisäys onnistui!")

    def aseta_satunnaiset_pisteet(self):
        self.lahtopiste, self.paatospiste = self.matriisi.anna_satunnaiset_pisteet()
        print(f"Asetettu lähtö: {self.lahtopiste}, päätös: {self.paatospiste}")

    def kysy_koordinaatit(self):
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            return self.matriisi.arvo((x,y)), (x, y)
        except ValueError:
            print(VIRHE)
            return None, None

    def suorituskyky(self):
        ku = Kuvaaja()
        ku.luo_algoritmien_aikavertailu(self.kuva.anna_tiedostonimi(), Heuristiikka.ESTEETON)
        ku.luo_algoritmien_aikavertailu(self.kuva.anna_tiedostonimi(), Heuristiikka.PYTHAGORAS)
        ku.luo_heuristiikan_aikavertailu(self.kuva.anna_tiedostonimi(), Algoritmi.A_STAR)
        ku.luo_heuristiikan_aikavertailu(self.kuva.anna_tiedostonimi(), Algoritmi.JPS)
        ku.luo_heuristiikkojen_solmuvertailu(self.kuva.anna_tiedostonimi(), Algoritmi.A_STAR)
        ku.luo_heuristiikkojen_solmuvertailu(self.kuva.anna_tiedostonimi(), Algoritmi.JPS)

vakio_ui = Ui()
