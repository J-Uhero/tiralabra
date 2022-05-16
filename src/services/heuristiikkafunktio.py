from math import sqrt
from enums.heuristiikka import Heuristiikka
# pylint: disable=unsubscriptable-object

SQRT2 = sqrt(2)

class Heuristiikkafunktio():
    """Luokka vastaa funktioista, joilla algoritmit laskevat eri heuristiikoilla
    h-arvon eli hypoteettisen etäisyyden tarkasteltavasta solmusta maalisolmuun.
    """
    def pythagoras(mista, minne):
        """Laskee pisteiden välissen euklidisen etäisyyden pythagoran lauseella

        Args:
            mista (tuple): (x,y)
            minne (tuple): (x,y)

        Returns:
            float: euklidinen etäisyys
        """
        return sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)

    def manhattan(mista, minne):
        """Laskee pisteiden välisen Manhattan-etäisyyden

        Args:
            mista (tuple): (x,y)
            minne (tuple): (x,y)

        Returns:
            float: Manhattan-etäisyys
        """
        return abs(mista[0] - minne[0]) + abs(mista[1] - minne[1])

    def esteeton(mista, minne):
        """Laskee etäisyyden, joka pisteiden välillä olisi, jos niiden välissä
        ei ole esteitä, kun eteneminen kartassa/verkossa tapahtuu kahdeksaan
        eri suuntaan diagonaalisesti tai vaaka-/pystysuunnassa.

        Args:
            mista (tuple): (x,y)
            minne (tuple): (x,y)

        Returns:
            float: esteetön etäisyys
        """
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
        return Heuristiikkafunktio.pythagoras
