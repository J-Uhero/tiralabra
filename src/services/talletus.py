from services.csv_lukija import vakio_csv_lukia as lukija

class Talletus:
    
    def talleta_lista(self, nimi, lista):
        return lukija.talleta_tiedostoon(nimi, lista)
    
    def palauta_rivi(self, algoritmi, heuristiikka, mista, minne, matka, aika, solmuja):
        return [algoritmi, heuristiikka, mista, minne, matka, aika, solmuja]

    def talleta_rivi(self, nimi, algoritmi, heuristiikka, mista, minne, matka, aika, solmuja):
        rivi = [algoritmi, heuristiikka, mista, minne, matka, aika, solmuja]
        return lukija.talleta_tiedostoon(nimi, rivi)
    
    def palauta_lista(self, nimi):
        return lukija.lue_tiedosto(nimi)

vakio_talletus = Talletus()
