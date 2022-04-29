from ui.ui import vakio_ui
from services.kuva import Kuva
from services.analysoi import Analysoi
import time

def main():
    ui = vakio_ui
    ui.aloita()

if __name__ == "__main__":
    main()
    """
    t = time.time()
    
    kuva = Kuva()
    matriisi = Analysoi(kuva)
    
    matriisi.alusta_matriisi()
    print("matriisi alustus", time.time()-t)
    t = time.time()
    print(matriisi.muuta_matriisiksi())
    print("matriisi covenrt", time.time()-t)
    t = time.time()
    print(matriisi.arvo((100,100)))
    a = time.time()-t
    #matriisi.tulosta()
    t = time.time()
    print(matriisi.np_arvo((100,100)))
    b = time.time()-t
    print("erotus", b-a)
    matriisi.tulosta_matriisi()
    """
    """
    print(matriisi.arvo((100,100)))
    print("150, 150", matriisi.arvo((150,150)))
    print("300, 300", matriisi.arvo((300,300)))
    print("550, 550", matriisi.arvo((550,550)))
    t = time.time()
    #print(kuva.vertaa_arvoa((0,0), 0))
    for y in range(1000):
        for x in range(1000):
            matriisi.arvo((x,y))
    print("matriisi arvo", time.time()-t)
    t = time.time()
    #print(kuva.vertaa_arvoa((0,0), 0))
    for y in range(1000):
        for x in range(1000):
            matriisi.np_arvo((100, 100))
    print("matriisi np arvo", time.time()-t)
    """
   

    
