from math import sqrt
from services.heuristiikka import Heuristiikka

SQRT2 = sqrt(2)

# pylint: disable=unsubscriptable-object
class Heuristiikkafunktio():
    """Luokka vastaa funktioista, joilla algoritmit laskevat eri heuristiikoilla
    h-arvon eli hypoteettisen etäisyyden tarkasteltavasta solmusta maalisolmuun.
    """
    def pythagoras(mista, minne):
        return sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)
    
    def manhattan(mista, minne):
        return abs(mista[0] - minne[0]) + abs(mista[1] - minne[1])
    
    def esteeton(mista, minne):
        x_e = abs(mista[0] - minne[0]) # solmujen x-koordinaattien etäisyys
        y_e = abs(mista[1] - minne[1]) # solmujen y-koordinaattien etäisyys
        return abs(x_e - y_e) + SQRT2 * min(x_e, y_e)

    def palauta_heuristiikkafunktio(heuristiikka):
        if heuristiikka == Heuristiikka.PYTHAGORAS:
            return Heuristiikkafunktio.pythagoras
        if heuristiikka == Heuristiikka.MANHATTAN:
            return Heuristiikkafunktio.manhattan
        if heuristiikka == Heuristiikka.ESTEETON:
            return Heuristiikkafunktio.esteeton
