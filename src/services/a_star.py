from heapq import heappop, heappush
import math

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

    def aloita(self, mista, minne, m, h):
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
        if m[mista[1]][mista[0]] or m[minne[1]][minne[0]]:
            return [], None, -1

        keko = []
        heappush(keko, (0, mista))
        edeltajat = {}
        g = {}
        g[mista] = 0
        f = {}
        f[mista] = h(mista, minne)
        sqrt2 = math.sqrt(2)

        while len(keko) > 0:
            nyk = heappop(keko)
            if nyk[1] == minne:
                return self.reitti(edeltajat, minne), edeltajat, g[minne]

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, koord_lisaykset_1):
                mahd_g = g[nyk[1]] + 1
                if seur_k not in g.keys():
                    g[seur_k] = math.inf
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    f[seur_k] = f_arvo
                    edeltajat[seur_k] = nyk[1]
                    heappush(keko, (f_arvo, seur_k))

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, koord_lisaykset_sqrt2):
                mahd_g = g[nyk[1]] + sqrt2
                if seur_k not in g.keys():
                    g[seur_k] = math.inf
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    f[seur_k] = f_arvo
                    edeltajat[seur_k] = nyk[1]
                    heappush(keko, (f_arvo, seur_k))
        return [], None, -1
