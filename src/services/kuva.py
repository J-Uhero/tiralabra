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
        self.tiedostonimi = tiedostonimi
        self.polku = os.path.dirname(__file__)
        self.tiedosto = None
        self.alk_kuva = None
        self.kuva = None
        self.lataa_kuva(self.tiedostonimi)

    def lataa_kuva(self, tiedostonimi):
        try:
            tiedosto = os.path.join(self.polku, "..", "data", tiedostonimi)
            self.alk_kuva = Image.open(tiedosto)
            self.kuva = self.alk_kuva.convert("L")
            self.tiedosto = tiedosto
            return True
        except:
            return False
    
    def anna_tiedostonimi(self):
        return self.tiedostonimi
    
    def aseta_kuvatiedosto(self, tiedostonimi):
        self.tiedosto = os.path.join(self.polku, "..", "data", tiedostonimi)

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
    
    def nayta_vareissa(self, kuva):
        kuva.show()
    
    def tulosta_a_star(self, reitti, edeltajat):
        kuva = self.alk_kuva.copy()
        for solmu in edeltajat.keys():
            self.varjaa_solmu(kuva, solmu, (250,200,200))
        self.piirra_vareissa(kuva, reitti)
        self.nayta_vareissa(kuva)
    
    def tulosta_jps(self, reitti, edeltajat):
        kuva = self.alk_kuva.copy()
        for seuraaja, edeltaja in edeltajat.items():
            self.piirra_vareissa(kuva, [seuraaja, edeltaja], vari=(250,200,200))
        self.piirra_vareissa(kuva, reitti)
        self.nayta_vareissa(kuva)

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
    
    def varjaa_solmu(self, kuva, koord, vari):
        kuva.putpixel(koord, vari)
    
    def piirra_vareissa(self, kuva, pisteet, vari="red"):
        piirra = ImageDraw.Draw(kuva)
        piirra.line(pisteet, width=1, fill=vari)
