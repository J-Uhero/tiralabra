import os
from PIL import Image, ImageDraw

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
        except FileNotFoundError:
            return False

    def anna_tiedostonimi(self):
        return self.tiedostonimi

    def aseta_kuvatiedosto(self, tiedostonimi):
        self.tiedosto = os.path.join(self.polku, "..", "data", tiedostonimi)

    def vertaa_arvoa(self, koord, arvo):
        return self.kuva.getpixel((koord)) == arvo

    def nayta_vareissa(self, kuva):
        kuva.show()

    def tulosta_a_star(self, reitti, edeltajat):
        """Piirtää kuvan A*-algoritmin löytämästä reitistä ja
        läpikäydytyistä solmuista

        Args:
            reitti (list): lyhin reitti
            edeltajat (dict): läpikäydyt solmut
        """
        kuva = self.alk_kuva.copy()
        for solmu in edeltajat.keys():
            self.varjaa_solmu(kuva, solmu, (250,200,200))
        self.piirra_vareissa(kuva, reitti)
        self.nayta_vareissa(kuva)

    def tulosta_jps(self, reitti, edeltajat):
        """piirtää ja näyttää kuvan JPS-algoritmin reitistä
        ja reiteistä löydettyihin jump pointeihin

        Args:
            reitti (list): lyhin reitti
            edeltajat (dict): läpikäydyt jump pointit
        """
        kuva = self.alk_kuva.copy()
        for seuraaja, edeltaja in edeltajat.items():
            if self.ei_kulmasolmua(seuraaja, edeltaja):
                self.piirra_vareissa(kuva, [seuraaja, edeltaja], vari=(250,200,200))
            else:
                kulma = self.hae_kulmasolmu(edeltaja, seuraaja)
                self.piirra_vareissa(kuva, [seuraaja, kulma], vari=(250,200,200))
                self.piirra_vareissa(kuva, [kulma, edeltaja], vari=(250,200,200))
        self.piirra_vareissa(kuva, reitti)
        self.nayta_vareissa(kuva)

    def ei_kulmasolmua(self, seuraaja, vanhempi):
        x_e = seuraaja[0]-vanhempi[0]
        y_e = seuraaja[1]-vanhempi[1]
        if abs(x_e) == abs(y_e) or \
                seuraaja[0] == vanhempi[0] or seuraaja[1] == vanhempi[1]:
            return True
        return False

    def hae_kulmasolmu(self, vanhempi, seuraaja):
        """Hakee kahden jump pointin j´välisen kulmasolmun
        visualisointia varten

        Args:
            vanhempi (tuple): (x,y)
            seuraaja (tuple): (x,y)

        Returns:
            tuple: kulmasolmu (x,y)
        """
        x_e = seuraaja[0]-vanhempi[0]
        y_e = seuraaja[1]-vanhempi[1]
        kulma = None
        if abs(x_e) > abs(y_e):
            if x_e > 0:
                kulma = (vanhempi[0]+abs(y_e), seuraaja[1])
            else:
                kulma = (vanhempi[0]-abs(y_e), seuraaja[1])
        else:
            if y_e > 0:
                kulma = (seuraaja[0], vanhempi[1]+abs(x_e))
            else:
                kulma = (seuraaja[0], vanhempi[1]-abs(x_e))
        return kulma

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
        """Värjää yksittäisen solmun

        Args:
            kuva (image): kuva, johon piirretään
            koord (tuple): piirrettävän solmun koordinaatti (x,y)
            vari (tuple): RGB-väri, jolla piirretään
        """
        kuva.putpixel(koord, vari)

    def piirra_vareissa(self, kuva, pisteet, vari="red"):
        """Piirtää reitin usean solmun välille

        Args:
            kuva (image): kuva, johon piirretään
            pisteet (list): reitti listana
            vari (str): käytettävä väri. Defaults to "red".
        """
        piirra = ImageDraw.Draw(kuva)
        piirra.line(pisteet, width=1, fill=vari)

    def anna_kuva(self):
        return self.alk_kuva.copy()
