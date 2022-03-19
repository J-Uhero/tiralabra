# Määrittelydokumentti

### Ohjelmointikieli
Toteutan projektini Pythonilla, joka on viime aikoina ollut minun pääasiallinen ohjelmointikieleni. Minulla on myös kokemusta Javasta, jota olen viimeksi käyttänyt vajaa pari vuotta sitten eikä se ole tuoreimmassa muistissa, joten ensisijaisesti haluaisin vertaisarvioida Python-projekteja.

### Opinto-ohjelma
Tietojenkäsittelytieteen kandiohjelma

### Aihe
Työssäni hyödynnän A*- ja JPS-reitinhakualgoritmeja. Algoritmeilla etsin lyhimmän reitin kaksiulotteisessa luolastossa ja vertailen algoritmeja ja niiden tehokkuutta keskenään. Valitsin tämän aiheen, koska jokin reitinhakuprojekti tuntui kiinnostavalta ja mahdolliselta aiheelta ja juteltuani kurssin ohjaajan kanssa aihe täsmentyi luolastoreitinhauksi. Kyseisiä algoritmeja käytän, koska en ole käyttänyt nimenomaisia algoritmeja aiemmin, vaikka tosin Dijkstran algoritmi on tuttu, johon A*:llä on yhtäläisyyttä.
Tarkoituksena on luoda ohjelma, jolle maaritellään jokin 2D-pikseligrafiikalla toteutettu luolasto, saa syötteenään koordinaatit, joiden välillä algoritmit hakevat lyhimmät reitit kiertäen luolaston seiniä. 
A*-algoritmin aikavaativuus on O(b^d) [lähde](https://en.wikipedia.org/wiki/A*_search_algorithm#Complexity), jossa b on branching factor eli keskimääräinen seuraajasolmujen lukumäärä ja d on lyhimmän reitin syvyys. JPS-algoritmin aikavaativuudelle en löytänyt mitään luotettavan oloista lähdettä, mutta se selvinnee projektin edetessä kun tutustun sen toimintaan.

### Dokumentaation kieli
Käytän dokumentaatiossa kielenäni suomea. Projektia alustaessani käytin commit-viesteissäni englantia, koska aiemmin minua on siihen ohjattu.
