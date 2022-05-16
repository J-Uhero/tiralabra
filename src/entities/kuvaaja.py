import matplotlib.pyplot as plt
from enums.algortimi import Algoritmi
from enums.heuristiikka import Heuristiikka
from repository.talletus import vakio_talletus as talletus
# pylint: disable=invalid-name

class Kuvaaja:
    """Luokka, joka luo kuvajat suorituskykytestauksesta
    """

    def luo_algoritmien_aikavertailu(self, nimi, heuristiikka):
        """Luo kuvaajan, joka vertailee algoritmien välistä matka/aika-eroa
        tietyllä heuristiikalla

        Args:
            nimi (str): kuvatiedoston nimi
            heuristiikka (enum): kaytettävä heuristiikka
        """
        h = str(heuristiikka)
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for rivi in talletus.palauta_lista(nimi):
            if rivi[1] == h:
                if rivi[0] == str(Algoritmi.A_STAR):
                    x1.append(float(rivi[4])) # 4: matka, 5: aika, (6: solmuja)
                    y1.append(float(rivi[5]))
                if rivi[0] == str(Algoritmi.JPS):
                    x2.append(float(rivi[4]))
                    y2.append(float(rivi[5]))
        otsikko = f"A* ja JPS aikavertailu, heuristiikka: {heuristiikka.value}"
        self.luo_scatter("matka", "aika (s)", "A*", "JPS", otsikko, x1, y1, x2, y2)

    def luo_heuristiikan_aikavertailu(self, nimi, algoritmi):
        """Luo kuvaajan, joka vertailee matka/aika-eroa eri heuristiikkojen
        välillä tietyllä algoritmilla

        Args:
            nimi (str): kuvatiedoston nimi
            algoritmi (enum): kaytettävä algoritmi
        """
        a = str(algoritmi)
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for rivi in talletus.palauta_lista(nimi):
            if rivi[0] == a:
                if rivi[1] == str(Heuristiikka.PYTHAGORAS):
                    x1.append(float(rivi[4])) # 4: matka, 5: aika, (6: solmuja)
                    y1.append(float(rivi[5]))
                if rivi[1] == str(Heuristiikka.ESTEETON):
                    x2.append(float(rivi[4]))
                    y2.append(float(rivi[5]))
        otsikko = f"Heuristiikan aikavertailu, algoritmi: {algoritmi.value}"
        self.luo_scatter("matka", "aika (s)", "pythagoras", "esteetön", otsikko, x1, y1, x2, y2)

    def luo_heuristiikkojen_solmuvertailu(self, nimi, algoritmi):
        """Vertailee vierailtujen solmujen määrä suhteessa matkan pituuteen
        eri heuristiikkojen välillä käytettäessä tiettyä algoritmia

        Args:
            nimi (str): kuvatiedoston nimi
            algoritmi (enum): käytettävä algoritmi
        """
        a = str(algoritmi)
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for rivi in talletus.palauta_lista(nimi):
            if rivi[0] == a:
                if rivi[1] == str(Heuristiikka.PYTHAGORAS):
                    x1.append(float(rivi[6])) # 4: matka, 5: aika, (6: solmuja)
                    y1.append(float(rivi[4]))
                if rivi[1] == str(Heuristiikka.ESTEETON):
                    x2.append(float(rivi[6]))
                    y2.append(float(rivi[4]))
        otsikko = f"Heuristiikan solmumäärävertailu, algoritmi: {algoritmi.value}"
        self.luo_scatter("solmuja", "matka", "pythagoras", "esteetön", otsikko, x1, y1, x2, y2)

    def luo_scatter(self, x_akseli, y_akseli, a, b, otsikko, x1, y1, x2, y2):
        """Luo kuvaajan

        Args:
            x_akseli (str): x-akselin kuvaus
            y_akseli (str): y-akselin kuvaus
            a (str): kuvaus, mitä verrataan
            b (str): kuvaus, mihin verrataan
            otsikko (str): kuvaajan otsikko
            x1 (list): lista a:n x-akselin arvoista
            y1 (list): lista a:n y-akselin arvoista
            x2 (list): lista b:n x-akselin arvoista
            y2 (list): lista b:n y-akselin arvoista
        """
        plt.scatter(x1, y1, label=a, color="blue", marker="o", s=1.5)
        plt.scatter(x2, y2, label=b, color="red", marker="o", s=1.5)
        plt.xlabel(x_akseli)
        plt.ylabel(y_akseli)
        plt.title(otsikko)
        plt.legend()
        plt.show()
