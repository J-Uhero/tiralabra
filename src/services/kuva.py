import os
from PIL import Image, ImageDraw
import numpy as np

KUVA = "Boston_1_1024.png"

class Kuva:
    """Luokka, jolla luodaan visualisointi kartasta ja reiteistä
    """
    def __init__(self, tiedostonimi=KUVA):
        """Luokan konstruktori

        Args:
            tiedostonimi (String): tiedostonimi kertoo tiedostonimen
            data-hakemistossa olevaan karttakuvaan, jota halutaan
            reitinhakuun käyttää.
        """
        polku = os.path.dirname(__file__)
        self.tiedosto = os.path.join(polku, "..", "data", tiedostonimi)
        self.alk_kuva = Image.open(self.tiedosto)
        self.kuva = self.alk_kuva.convert("L")

    def luo_np_taulukko(self):
        """Luo Numpy-kirjastolla matriisin, mikäli haluan käyttää
        kyseistä kirjastoa apuna
        """

        return np.array(self.kuva)
    
    def vertaa_arvoa(self, koord, arvo):
        return self.kuva.getpixel((koord)) == arvo

    def nayta(self):
        """Näytä kuva
        """
        self.kuva.show()
    
    def nayta_vareissa(self):
        self.alk_kuva.show()


    def kuvan_koko(self):
        """Palautetaan kuvan koko muodossa (x,y)

        Returns:
            tuple: (leveys, korkeus)
        """
        return self.kuva.size

    def piirra(self, pisteet):
        """Piirretään kuvaan reitti koorditaattipisteiden avulla

        Args:
            pisteet (list): lista (x,y)-muotoisista koordinaattitupleista,
            joiden väliin reitti piirretään
        """
        piirra = ImageDraw.Draw(self.kuva)
        piirra.line(pisteet, width=1, fill="red")
    
    def varjaa_solmu(self, koord, vari):
        self.alk_kuva.putpixel(koord, vari)
    
    def piirra_vareissa(self, pisteet):
        piirra = ImageDraw.Draw(self.alk_kuva)
        piirra.line(pisteet, width=1, fill="red")
