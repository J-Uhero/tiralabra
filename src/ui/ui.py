from services.algoritmi import a_tahti

class Ui:
    """Ohjelman käyttöliittymä. Käyttöliittymä kehittynee kurssin edetessä.
    Vaikka kerkesin jo hieman tutkia Pillow-kirjastoa ja suunnitella kartta-
    reittien piirtämistä, ajattelin kuitenkin tehdä aluksi pelkästään komento-
    riviltä suoritettavan ja ASCII-visualisoidun käyttöliittymän.
    """
    def __init__(self):
        #self.kuvanpiirtaja = Kuvanpiirtaja()
        pass

    def aloita(self):
        #self.kuvanpiirtaja.piirra()
        a_tahti((0,0), (4,3))

vakio_ui = Ui()