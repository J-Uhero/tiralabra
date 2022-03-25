from heapq import heappop, heappush
from queue import Empty
import math

m1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
    ]

def reitti(edeltajat, solmu):
    r = [solmu]
    while solmu in edeltajat.keys():
        solmu = edeltajat[solmu]
        r = solmu + r
    return r

def h_arvot(mista, minne):
    #h-arvo lasketaan suorana etäisyytenä päätepisteeseen pythagoran lauseella
    return math.sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)

def tarkista_sivukoordinaatit(solmu, m):
    p = []
    for k in [(0,-1), (0,1), (-1,0), (1,0)]:
        uusi = (k[0]+solmu[0], k[1]+solmu[1])
        if uusi[0] >= 0 and uusi[1] >= 0:
            if m[solmu[1],solmu[0]] == 0:
                p.append(uusi)
    return p

def a_tahti(mista, minne, h=h_arvot, m=m1):
    """Tämä on ensimmäinen versioni a*-algoritmista, joka vielä vaiheessa (key error)
    """
    keko = []
    heappush(keko, (0, mista)) #(f-arvo, (x,y))
    edeltajat = {}
    g = {}
    g[mista] = 0
    f = {}
    f[mista] = h(mista, minne)
    sqrt2 = math.sqrt(2)

    while keko is not Empty:
        nyk = heappop(keko)
        if nyk[1] == minne:
            return reitti(edeltajat, minne)
        for k in [(0,-1), (0,1), (-1,0), (1,0)]:
            print("matriisi arvo",m[k[1]+nyk[1][1]][k[0]+nyk[1][0]], k[1]+nyk[1][1], k[0]+nyk[1][0])  
            if m[k[1]+nyk[1][1]][k[0]+nyk[1][0]] == 0:
                seur_k = (k[1]+nyk[1][1],k[0]+nyk[1][0])
                mahd_g = g[nyk[1]] + 1
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    f[seur_k] = f_arvo
                    edeltajat[seur_k] = nyk[1]
                    if (f_arvo, seur_k) not in keko:
                        heappush(keko, (f_arvo, seur_k))

        for k in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            if m[k[1]+nyk[1][1]][k[0]+nyk[1][0]] == 0:
                seur_k = (k[1]+nyk[1][1],k[0]+nyk[1][0])
                mahd_g = g[nyk[1]] + sqrt2
                if mahd_g < g[seur_k]:
                    g[seur_k] = mahd_g
                    f_arvo = mahd_g + h(seur_k, minne)
                    f[seur_k] = f_arvo
                    edeltajat[seur_k] = nyk[1]
                    if (f_arvo, seur_k) not in keko:
                        heappush(keko, (f_arvo, seur_k))
    return None
