from heapq import heappop, heappush
import math
# pylint: disable=invalid-name

KOORD_LISAYKSET_1 = [(0,-1), (0,1), (-1,0), (1,0)]
KOORD_LISAYKSET_SQRT2 = [(-1,-1), (-1,1), (1,-1), (1,1)]

class A_star:
    """Luokka A*-algoritmille
    """

    def reitti(self, edeltajat, solmu):
        """haetaan algoritmin reitti edeltajat-hajautustaulusta
        päätesolmun avulla
        """
        reitti = [solmu]
        while solmu in edeltajat:
            solmu = edeltajat[solmu]
            reitti.append(solmu)
        reitti.reverse()
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

    def hyvaksytyt_koordinaatit(self, mista, minne, m):
        """Tarkastaa, että koordinaatit ovat matriisissa
        eivätkä osu esteeseen.

        Args:
            alku (tuple): (x,y)
            loppu (_type_): (x,y)
            m (list): matriisi

        Returns:
            boolean: totuusarvo koordinaattien kelpaavuudesta
        """
        if mista[0] < 0 or mista[0] >= len(m[0]) or mista[1] < 0 or mista[1] >= len(m):
            return False
        if minne[0] < 0 or minne[0] >= len(m[0]) or minne[1] < 0 or minne[1] >= len(m):
            return False
        if m[mista[1]][mista[0]] or m[minne[1]][minne[0]]:
            return False
        return True


    def aloita(self, mista, minne, m, h):
        """Käynnistää A*-algoritmin.

        Args:
            mista (tuple): (x,y)-muodossa lähtöpiste/-solmu
            minne (tuple): (x,y)-muodossa kohdepiste/-solmu
            m (list): matriisi eli lista listoja, jotka kuvaavat kartastoa ja
            sen pisteitä
            h (method): funktio heuristiikan eli h-arvon laskemiseen

        Palauttaa:
            tuple: reitti listana, sanakirja edeltäjäsolmuista, reitin pituus
        """

        if not self.hyvaksytyt_koordinaatit(mista, minne, m):
            return [], None, -1

        keko = []
        heappush(keko, (h(mista, minne), mista))
        edeltajat = {}
        g = {}
        g[mista] = 0
        sqrt2 = math.sqrt(2)

        while len(keko) > 0:
            nyk = heappop(keko)
            if nyk[1] == minne:
                return self.reitti(edeltajat, minne), edeltajat, g[minne]

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, KOORD_LISAYKSET_1):
                mahd_g = g[nyk[1]] + 1
                if seur_k not in g:
                    g[seur_k] = math.inf
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    edeltajat[seur_k] = nyk[1]
                    heappush(keko, (f_arvo, seur_k))

            for seur_k in self.tarkista_koordinaatit(nyk[1], m, KOORD_LISAYKSET_SQRT2):
                mahd_g = g[nyk[1]] + sqrt2
                if seur_k not in g:
                    g[seur_k] = math.inf
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    edeltajat[seur_k] = nyk[1]
                    heappush(keko, (f_arvo, seur_k))
        return [], None, -1
