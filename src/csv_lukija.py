import csv
import os

POLKU = os.path.dirname(__file__)

class CSVLukija:
    """Luokka, joka toimii rajapintana CSV-tiedoston ja ohjelman välillä.
    Sen avulla talletetaan ja luetaan tietoa algoritmien
    ajosta CSV-tiedostoon suorituskykytestausta varten
    """

    def tiedostonimi(self, nimi):
        """Palauttaa tiedostonimen kokonaisena polkuna

        Args:
            nimi (str): merkkijonona pelkkä kuvatiedoston nimi
        Returns:
            str: nimi kokonaisena polkuna
        """
        return os.path.join(POLKU, "data", nimi + ".csv")

    def lue_tiedosto(self, nimi):
        rivit = []
        try:
            with open(self.tiedostonimi(nimi)) as tiedosto:
                for rivi in csv.reader(tiedosto, delimiter=";"):
                    rivit.append(rivi)
        except FileNotFoundError:
            print("CSV-tiedostonimen lukeminen ei onnistunut")
            return None
        return rivit

    def talleta_tiedostoon(self, nimi, rivit):
        try:
            with open(self.tiedostonimi(nimi), "a") as tiedosto:
                kirjuri = csv.writer(tiedosto, delimiter=";")
                for rivi in rivit:
                    kirjuri.writerow(rivi)
            return True
        except FileNotFoundError:
            print("CSV-tiedostoon talletus ei onnistunut")
            return False

vakio_csv_lukija = CSVLukija()
