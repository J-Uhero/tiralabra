import matplotlib.pyplot as plt
from random import randint
from services.algortimi import Algoritmi
from services.heuristiikka import Heuristiikka
from services.talletus import vakio_talletus as talletus

class Kuvaaja:

    def luo_algoritmien_aikavertailu(self, nimi, heuristiikka):
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
        self.luo_scatter("matka", "aika (s)", "A*", "JPS", otsikko, nimi, x1, y1, x2, y2)

    def luo_heuristiikan_aikavertailu(self, nimi, algoritmi):
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
        self.luo_scatter("matka", "aika (s)", "pythagoras", "esteetön", otsikko, nimi, x1, y1, x2, y2)

    def luo_heuristiikkojen_solmuvertailu(self, nimi, algoritmi):
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
        self.luo_scatter("solmuja", "matka", "pythagoras", "esteetön", otsikko, nimi, x1, y1, x2, y2)

    def luo_scatter(self, x_akseli, y_akseli, a, b, otsikko, nimi, x1, y1, x2, y2):
        plt.scatter(x1, y1, label=a, color="blue", marker="o", s=1.5)
        plt.scatter(x2, y2, label=b, color="red", marker="o", s=1.5)
        plt.xlabel(x_akseli)
        plt.ylabel(y_akseli)
        plt.title(otsikko)
        plt.legend()
        plt.show()
