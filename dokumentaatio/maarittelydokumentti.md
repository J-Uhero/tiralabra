# Määrittelydokumentti

## Ohjelmointikieli
Toteutan projektini Pythonilla, joka on viime aikoina ollut minun pääasiallinen ohjelmointikieleni. Minulla on myös kokemusta Javasta, joka tosin ei ole tuoreimmassa muistissa, joten ensisijaisesti haluaisin vertaisarvioida Python-projekteja.

## Opinto-ohjelma
Tietojenkäsittelytieteen kandiohjelma

## Aihe
Työssäni hyödynnän A*- ja JPS eli Jump Point Search -reitinhakualgoritmeja. Algoritmeilla etsin lyhimmän reitin kaksiulotteisessa kartassa/matriisissa sekä vertailen algoritmeja ja niiden tehokkuutta keskenään. Valitsin tämän aiheen, koska jokin reitinhakuprojekti tuntui kiinnostavalta ja mahdolliselta aiheelta. Juteltuani kurssin ohjaajan kanssa aiheeksi täsmentyi tämänkaltainen karttareitinhaku käyttäen kyseisiä algoritmeja. Päädyin A*- ja JPS-algoritmeihin, koska JPS-algoritmi on ilmeisimmin omiaan juuri tähän tarkoitukseen enkä ole käyttänyt nimenomaisia algoritmeja aiemmin, vaikka tosin Dijkstran algoritmi, johon A*:llä on yhtäläisyyttä, on tuttu. 
Tarkoituksena on luoda ohjelma, jolle maaritellään jokin 2D-pikseligrafiikalla tai matriisina toteutettu kartta, jossa on esteitä. Ohjelma saa syötteenään koordinaatit, joiden välillä algoritmit hakevat lyhimmät reitit kartassa pisteestä toiseen kulkematta esteisiin. Ohjelma esittää visuaalisesti kartan ja reitit.
A*-algoritmin aikavaativuus on O(b^d) ([lähde](https://en.wikipedia.org/wiki/A*_search_algorithm#Complexity)), jossa b on branching factor eli keskimääräinen seuraajasolmujen lukumäärä ja d on lyhimmän reitin syvyys. JPS-algoritmin aikavaativuudelle en löytänyt mitään luotettavan oloista lähdettä, mutta se selvinnee projektin edetessä tutustuttuani algoritmin toimintaan.

## Dokumentaation kieli
Käytän dokumentaatiossa kielenäni suomea. Projektia alustaessani käytin commit-viesteissäni englantia, koska aiemmin minua on siihen ohjeistettu.
