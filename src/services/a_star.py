from heapq import heappop, heappush
import math
from services.heuristiikkafunktio import Heuristiikkafunktio as hf

koord_lisaykset_1 = [(0,-1), (0,1), (-1,0), (1,0)]
koord_lisaykset_sqrt2 = [(-1,-1), (-1,1), (1,-1), (1,1)]

class A_star:

    def reitti(self, edeltajat, solmu):
        """haetaan algoritmin reitti edeltajat-hajautustaulusta
        päätesolmun avulla
        """
        reitti = [solmu]
        while solmu in edeltajat.keys():
            solmu = edeltajat[solmu]
            reitti = [solmu] + reitti
        return reitti

    def h_arvot(mista, minne):
        """h-arvo lasketaan suorana etäisyytenä päätepisteeseen pythagoran
        lauseen avulla. H-arvo kertoo arvion, mikä voisi olla jäljellä olevan
        reitin pituus nykyisestä solmusta käsin ja on tässä tapauksessa
        täysin suora reitti.
        """

        return math.sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)

    def tarkista_koordinaatit(self, solmu, m, koord_lisaykset):
        """A*-algoritmin hyödyntämä funktio tarkistamaan,
        mihin solmuihin/pisteisiin nykyisestä solmusta/pisteestä
        voi siirtyä. Etsii joko sivuttaiset tai kulmittaiset solmut/pikselit.

        Args:
            solmu (tuple): nykyinen solmu (x,y)-muodossa.
            m (list): matriisi solmuista eli lista listoja
            koord_lisaykset (list): lista lisäyksistä koordinaatteihin
            riippuen, haetaanko sivuttaiset vai kulmittaiset solmut.

        Palauttaa:
            lista: lista (x,y)-tuplekoordinaatteja kuvaten siirryttäviä
            solmuja.
        """

        p = []
        for k in koord_lisaykset:
            uusi = (k[0]+solmu[0], k[1]+solmu[1])
            if (len(m[0]) > uusi[0] >= 0) and (len(m) > uusi[1] >= 0):
                if m[uusi[1]][uusi[0]] == 0:
                    p.append(uusi)
        return p

    def aloita(self, mista, minne, m, h=h_arvot):
        """A*-algoritmi. Näyttäisi toimivan nyt oikein.
        Vaatinee vielä optimointia ja toisteisen koodin siismistä.

        Args:
            mista (tuple): (x,y)-muodossa lähtöpiste/-solmu
            minne (tuple): (x,y)-muodossa kohdepiste/-solmu
            h (funktio): Funktio, jolla lasketaan h-arvo. Oletuksena h_arvot.
            m (list): matriisi eli lista listoja, jotka kuvaavat kartastoa ja
            sen pisteitä. Oletuksena m1.

        Palauttaa:
            Reitti-funktion, ja sen palautusarvot, jos reitti löydetään tai None,
            jos reittiä ei löydetä.
        """

        keko = []
            # alustetaan keko, johon tallennetaan tarkasteltavat solmut, niin että
            # pienimmän f-arvon solmu otetaan sieltä aina seuraavana tarkasteluun.
            # talletukset ovat siis muotoa: (f-arvo, (x,y))
        heappush(keko, (0, mista))
            # lähtösolmun alustus.
        edeltajat = {}
            # hajautustaulu solmujen edeltäjäsolmujen talletusta varten
        g = {}
            # talletettavat g-arvot eli lyhimmän löydetty reittin pituus solmuun
        g[mista] = 0
            # alkusolmun g-arvo eli 0
        f = {}
            # talletettavat f-arvot eli g + h, jossa h on arvio jäljellä olevan
            # reitin pituudesta
        f[mista] = h(mista, minne)
            # alkusolmun f-arvo eli 0 + h-arvo
        sqrt2 = math.sqrt(2)
            # neliöjuuri 2 valmiina muuttujassa

        while len(keko) > 0:
            nyk = heappop(keko)
                # nykyinen solmu on keon seuraava solmu pienimmällä f-arvolla
            if nyk[1] == minne:
                # tarkastetaan, onko määränpää-solmu saavutettu, jolloin
                # reitti on löydetty
                return self.reitti(edeltajat, minne), edeltajat, g[minne]
                    # palautetaan reitti-funktio, joka palauttaa lyhimmän reitin
                    # listana tuplekoordinaatteja

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, koord_lisaykset_1):
                # tarkistetaan mahdolliset seuraajasolmujen koordinaatit ja
                # käydään ne yksittäin läpi. tarkasteltavat solmut ovat tässä
                # for-silmukassa nykyisen solmun sivujen myötäisiä ja niiden
                # etäisyys on näin ollen 1
                mahd_g = g[nyk[1]] + 1
                    # seuraavan solmun mahdollinen g-arvo, kun solmu on sivuttain nykyiseen
                if seur_k not in g.keys():
                    g[seur_k] = math.inf
                        # alustetaan uusien solmujen vertailtavaksi
                        # g-arvoksi (etäisyys lähtösolmusta) inf eli ääretön
                if mahd_g < g[seur_k]:
                        # tehdään vertailu, onko jo löydetty g-arvo suurempi kuin uusi, jolloin
                        # uusi arvo halutaan vaihtaa vanhan tilalle
                    g[seur_k] = mahd_g
                        # aiempi mahdollinen g-arvo vaihdetaan nykyiseksi, jos se oli pienempi eli
                        # solmuun löydettiin lyhyempi reitti
                    f_arvo = mahd_g + h(seur_k, minne)
                        # f = g + h eli f-arvo on jo löydetty reitti + arvio jäljellä olevasta reitistä
                    f[seur_k] = f_arvo
                        # asetetaan solmun f-arvo f-taulukkoon
                    edeltajat[seur_k] = nyk[1]
                        # talletetaan seuraajasolmun edeltäjäsolmun koordinaatit muistiin
                    #if (f_arvo, seur_k) not in keko:
                    heappush(keko, (f_arvo, seur_k))
                            # solmu laitetaan kekoon, josta pääsilmukassa otetaan solmuja
                            # pienimmän f-arvon mukaan.

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, koord_lisaykset_sqrt2):
                # tässä for-silmukassa toteutetaan samat asiat kuin aiemmassa, mutta tarkasteltavat
                # solmut ovat kulmikkain nykysolmuun nähden, jolloin reitin pituus kasvaa
                # yhden sijaan neliöjuuri kahdella
                mahd_g = g[nyk[1]] + sqrt2
                if seur_k not in g.keys():
                    g[seur_k] = math.inf
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    f[seur_k] = f_arvo
                    edeltajat[seur_k] = nyk[1]
                    #if (f_arvo, seur_k) not in keko:
                    heappush(keko, (f_arvo, seur_k))
        return None
            # tyhjä palautus, jos reittiä ei löytynyt tarkasteltavien solmujen loppuessa kesken
