from PIL import Image, ImageDraw
import numpy as np
import os

KUVA = "Boston_1_1024.png"

class Kuvanpiirtaja:
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
        tiedosto = os.path.join(polku, "..", "data", tiedostonimi)
        self.kuva = Image.open(tiedosto)
        self.piirra(0,0)

    def luo_np_taulukko(self):
        """Luo Numpy-kirjastolla matriisin, mikäli haluan käyttää
        kyseistä kirjastoa apuna
        """
        self.taulukko = np.array(self.img)

    def nayta(self):
        """Näytä kuva
        """
        self.kuva.show()
    
    def kuvan_koko(self):
        """Palautetaan kuvan koko muodossa (x,y)

        Returns:
            tuple: (leveys, korkeus)
        """
        return self.kuva.size()

    def piirra(self, pisteet):
        """Piirretään kuvaan reitti koornitaattipisteiden avulla

        Args:
            pisteet (list): lista (x,y)-muotoisista koordinaattitupleista,
            joiden väliin reitti piirretään
        """
        piirra = ImageDraw.Draw(self.img)
        piirra.line(pisteet, width=1, fill="red")
