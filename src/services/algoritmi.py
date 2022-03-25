from heapq import heappop, heappush
import math

m1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
    ]

m2 = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0]
    ]

koord_lisaykset_1 = [(0,-1), (0,1), (-1,0), (1,0)]
koord_lisaykset_sqrt2 = [(-1,-1), (-1,1), (1,-1), (1,1)]

def reitti(edeltajat, solmu):
    """haetaan algoritmin reitti edeltajat-hajautustaulusta"""
    r = [solmu]
    while solmu in edeltajat.keys():
        solmu = edeltajat[solmu]
        r = [solmu] + r
    return r

def luo_reittimatriisi(m, reitti):
    uusi_m = list(m)
    for k in reitti:
        uusi_m[k[1]][k[0]] = 2
    return uusi_m

def tulosta_matriisi(m):
    for i in range(len(m)):
        print(m[i])

def h_arvot(mista, minne):
    """h-arvo lasketaan suorana etäisyytenä päätepisteeseen pythagoran lauseella
    """
    return math.sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)

def tarkista_koordinaatit(solmu, m, koord_lisaykset):
    p = []
    for k in koord_lisaykset:
        uusi = (k[0]+solmu[0], k[1]+solmu[1])
        if (len(m[0]) > uusi[0] >= 0) and (len(m) > uusi[1] >= 0):
            if m[uusi[1]][uusi[0]] == 0:
                p.append(uusi)
    return p

def a_tahti(mista, minne, h=h_arvot, m=m1):
    """A*-algoritmi. Näyttäisi toimivan nyt oikein.
    Vaatinee vielä optimointia ja toisteisen koodin siismistä
    """
    keko = []
    heappush(keko, (0, mista)) #(f-arvo, (x,y))
    edeltajat = {}
    g = {}
    g[mista] = 0
    f = {}
    f[mista] = h(mista, minne)
    sqrt2 = math.sqrt(2)

    while len(keko) > 0:
        nyk = heappop(keko)
        print(nyk)
        if nyk[1] == minne:
            return reitti(edeltajat, minne)

        for seur_k in tarkista_koordinaatit(nyk[1], m, koord_lisaykset_1):
            mahd_g = g[nyk[1]] + 1
            if seur_k not in g.keys():
                g[seur_k] = math.inf
            if mahd_g < g[seur_k]:
                g[seur_k] = mahd_g
                f_arvo = mahd_g + h(seur_k, minne)
                f[seur_k] = f_arvo
                edeltajat[seur_k] = nyk[1]
                if (f_arvo, seur_k) not in keko:
                    heappush(keko, (f_arvo, seur_k))

        for seur_k in tarkista_koordinaatit(nyk[1], m, koord_lisaykset_sqrt2):
            mahd_g = g[nyk[1]] + sqrt2
            if seur_k not in g.keys():
                g[seur_k] = math.inf
            if mahd_g < g[seur_k]:
                g[seur_k] = mahd_g
                f_arvo = mahd_g + h(seur_k, minne)
                f[seur_k] = f_arvo
                edeltajat[seur_k] = nyk[1]
                if (f_arvo, seur_k) not in keko:
                    heappush(keko, (f_arvo, seur_k))
    return None
