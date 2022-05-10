from math import sqrt

class Heuristiikkafunktio():
    def pythagoras(mista, minne):
        return sqrt((mista[0]-minne[0])**2 + (mista[1]-minne[1])**2)
    
    def manhattan(mista, minne):
        return abs(mista[0] - minne[0]) + abs(mista[1] - minne[1])
    
    def esteeton(mista, minne):
        x_e = abs(mista[0] - minne[0]) # solmujen x-koordinaattien etäisyys
        y_e = abs(mista[1] - minne[1]) # solmujen y-koordinaattien etäisyys
        return abs(x_e - y_e) + sqrt(2) * min(x_e, y_e)
