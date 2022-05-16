# Toteutusdokumentti

Projektissa on toteutettu A* ja JPS algoritmit ja käyttöliittymä niiden ajamiseen ja testaamiseen sekä visualisointi Pillow-kirjastoa hyödyntäen. Suorituskykytestauksen graafit olen toteuttanut Mathplotlib-kirjaston avulla.

Olen algoritmien toteutuksessa oman harkintani mukaan tehnyt ratkaisuja, jotka ovat voineet poiketa alkuperäisestä pseudokoodista kuitenkin niin, että algoritmien toimintatapa on vastaava ja mielestäni asianmukainen. Projektin alussa mietin, miten kuvata solmuja ja kaaria, kun verkko on säännönmukainen matriisi tai pikselikartta. Sen sijaan, että olisin kuvannut kaaria jossain omassa tietorakenteessa, olen päätynyt tarkastamaan kaaret matriisista, johon on tallennettu, missä kohdissa verkkoa sen esteet ovat. Solmuilla on aina maksimissaan 8 naapurisolmua, joihin on vakioetäisyys ja joihin johtavat kaaret pystyn tarkastamaan koordinaateille tehtävillä yksinkertaisilla laskutoimituksilla. Tämä on mielestäni perusteltu toimintatapa, koska kaarien tarkastus tapahtuu aina vakioajassa eikä verkon, jossa voi olla yli miljoona solmua, alustaminen ole niin raskasta ja aikaavievää. Myöskään tilaa ei kulu niin paljon. Lisäksi A*:ssa ja JPS:ssä on eri naapurisolmut. JPS:ää käytettäessä tällä tavalla myös valtytään A*:n käyttämien naapurisolmujen karsisesta, joka on kuvattu Haraborin ja Grastien Online Graph Pruning for Pathfinding on Grid Maps -dokumentissa prune-funktiolla. Lisäksi siinä missä alkuperäisessä dokumentissa JPS hakee tai skannaa verkkoa etsien hyppypisteitä rekursiivisesti jump-funktion avulla, käytin itse while true -silmukkaa, jossa haku tapahtuu. Näin rekursio ei pääse kohtuuttoman syväksi ja haun päättyessä esteeseen tai verkon/kartan reunoihi, toimii silmukka vastaavalla tavalla kuin rekursiivisessa haussa. Laskin myös jump pointien väliset etäisyydet yhdellä kertaa sen sijaan, että olisin tehnyt lukuisia laskutoimituksia kasvattamalla etäisyyttä aina yhdellä tai kahden neliöjuurella.

Ohjelma noudattaa kansiorakenteeltaan Ohtesta tuttua repository-rakennetta. Ohjelmalogiikan kannalta ohjelman keskeisimmät asiat eli algoritmit on sijoitettu services-hakemistoon, jonka lisäksi src-hakemistosta löytyvät data-, entities-, repository-, tests-, ui- ja enums-hakemistot. Ohjelma käynnistetään src-hakemiston juuressa olevasta index.py-tiedostosta. Hakemistot ovat nimetty englanniksi repository-arkkitehtuurin mukaan.

A*:n aika- ja tilavaatimus on vaatimusmäärittelyssä mainitsemani O(b^d), jossa b on branching factor eli keskimääräinen seuraajasolmujen lukumäärä ja d on lyhimmän reitin syvyys. JPS käyttää myös pohjanaan A*:a joten aika- ja tilavaatimus on sinänsä sama, mutta seuraajasolmujen sijaan voisikin puhua seuraajahyppypisteistä, joden määrä riippuu tietysti verkosta, mutta niitä on pääsääntöisesti vähemmän kuin A*:n seuraajasolmuja, ellei verkosta haettava reitti ole todella lyhyt. Tämän voi huomata myös suorituskykytestauksesta, josta ilmenee, että A* toimii jopa JPS:ää nopeammin, kun lähtö- ja maalipisteiden etäisyys on lyhyimmillään. JPS-käyttää kuitenkin aikaa kartan tutkimiseen ja jump pointien etsimiseen ja tämä haku saattaa edetä laajalle, vaikka maalisolmu olisi lähellä.

![suorituskykytestaus4](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus4.png)

Vaikka varsinainen aihe oli vertailla keskenään A*- ja JPS-algoritmeja, halusin myös tutkia, miten erilaiset heuristiikat vaikuttavat algoritmin nopeuteen ja sen käsittelemien solmujen määrään. Ajatus tähän tuli, kun mietin miten Pythagoran lauseen ylioptimistinen euklidinen etäisyys suosii varsin paljon haun alkupään solmuja ja halusin kokeillaa heuristiikkana samaa funktiota, jolla laskin JPS:n jump pointien välisen esteettömän etäisyyden, joka on optimistinen, mutta kuitenkin mahdollinen todellinen etäisyys, mikäli esteiltä vältytään. Tätä vertailua on nähtävissä [testausdokumentista](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/testausdokumentti.md). Manhattan-etäisyydestä puolestaan huomasin, ettei se anna aina lyhintä reittiä, koska se on arviona pessimistinen ja suosii pysty- ja vaakatason reittejä. Jätin sen tämän tähden pois heuristiikkavertailuista, vaikka sen voi ohjelmassa halutessaan valita käyttöön asetuksista.

Parannusehdotuksena projektiini sanoisin, että A*:ia ja JPS:ää voisi yhdenmukaistaa siinä, ettei A* menisi diagonaalisesti sellaisiin solmuihin, joiden kummallakin puolella on esteet. Käyttäessäni karttadataa tällä ei kuitenkaan käytännössä ole ollut väliä, kun esteet ovat niissä suuria ja yhteneväisiä. Lisäksi olisi kiva vertailla algoritmejani samoihin algoritmeihin, mutta hieman eri tavoin toteutettuina. Esimerkiksi solmuja ja kaaria voisi kuvata näissä eri tavoin, jolloin olisi mielenkiintoista koittaa verrata, millainen toteutustapa algoritmille olisi optimaalisin. Lisäksi miettiessäni projektini etenemistä, olisi parempi, jos työmäärä jakautuisi tasaisemmin projektin aikana. Välillä eteneminen takkusi ja välillä taas työskentelin pitkään yhtenäisesti. Myös Git Hub -commitit voisivat olla selkeämpiä ja pienempiä kokonaisuuksia, kuin mitä ne välillä olivat. Kirjoitin myös koodini suomeksi, koska ymmärsin, että varsinaisen koodin tulee olla samalla kielellä kuin dokumentaatio eikä pelkästään koodin kommentoinnin. Englanti olisi luontevampi kieli koodille ja huomasin, että vertaisarvioimissani projekteissä koodi oli englanniksi, mutta dokumentaatio suomeksi. Koodin tietorakenteet ja vakiokirjastot ja -funktiot ovat kuitenkin englanniksi, joten koodista tulee suomeksi kirjoitettuna joka tapauksessa englannin ja suomen sekoitusta.

Lähteet:

* [A Visual Explanation of Jump Point Search, Nathan Witmer](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html)

* [A* Algorithm in AI | A Star Search Algorithm | Artificial Intelligence Tutorial | Edureka, _Youtube_.](https://www.youtube.com/watch?v=amlkE0g-YFU)

* [A* search algorithm, _Wikipedia_.](https://en.wikipedia.org/wiki/A*_search_algorithm)

* [A* Search Algorithm, _Geeks For Geeks_.](https://www.geeksforgeeks.org/a-search-algorithm/)

* [Implementation of A*, Amit Patel](https://www.redblobgames.com/pathfinding/a-star/implementation.html)

* [Jump Point Search: Fast A* Pathfinding for Uniform Cost Grids, Albert Hofkamp](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)

* [Online Graph Pruning for Pathfinding on Grid Maps, Harabor, D. and Grastien, A.](https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)

* [Single Agent Search Video 39: Canonical Orderings on Grids, Sturtevant N., Youtube](https://www.youtube.com/watch?v=rskXf8kO5Lw)

* [Single Agent Search Video 40: Jump Point Search and Other Algorithms Using Canonical Orderings, Sturtevant N., Youtube](https://www.youtube.com/watch?v=__ZLnTwYNPk)

Karttakuvan lähde:

https://www.movingai.com/benchmarks/grids.html (Real-World Benchmarks)
