# Viikkoraportti 3

Palasin sunnuntaina testailemaan toisen viikon aikaansaannosta eli A*-algoritmia. Testikattavuudessa algoritmista jäi kaksi if-haaraa tarkastamatta silloin, kun if-lauseiden ehto ei täyty. Kyseisissä haaroissa tarkastetaan, onko solmu jo lisätty kekoon ja jos on, se lisätään. Testitapauksissa ei siis käynyt niin, että jokin solmu olisi löytynyt jo keosta.

![if-haara](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/testien_ohittama_if_haara.png)

Yritin tehdä testitapauksia, joissa tämä haara tulisi läpikäydyksi. Tapaukseen, jossa tarkasteltava solmu on diagonaalisesti/kulmikkain nykyisen solmuun kanssa, onnistuin luomaan sellaisen testimatriisin, että solmu löytyy jo keosta ja haara tulee testatuksi.

Tapaukseen, jossa nykysolmuun nähden sivuttain oleva solmu olisi jo keossa, en onnistunut luomaan testimatriisia, vaikka yritin tehdä hirvittävän näköisiä sokkelomatriiseja, jotka yrittävät huijata algoritmia mahdollisimman paljon. Esimerkiksi tällainen kammotus:

![hirveä testimatriisi](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/hirvea_testimatriisi.png)

Rupesin tämän myötä miettimään toisen viikon A*-algoritmini ongelmia. Koska solmu talletetaan kekoon tuplena muodossa (f-arvo, (x, y)), if-lause ei tunnista solmua samaksi, mikäli verrattavan solmun f-arvo on eri kuin aiemmin lisätyn. Tämä mahdollistaa sen, että sama solmu lisätään kekoon useamman kerran, mikäli uudestaan lisättävälle solmulle on laskettu eri f-arvo kuin aiemmin. Mietin, miten ongelman kannattaisi ratkaista, koska solmut tulee nostaa keosta pienimmän f-arvon mukaan ja f-arvon täytyy näin ollen olla mukana. Tallettaako keossa olevat solmut vaikka erilliseen hajautustauluun. Jos solmuja on paljon keossa, sen sisällön tarkastaminen on myös aikaa vievää, joten se voisi olla siinä mielessä nopeampi, vaikkakin enemmän tilaa vievä ratkaisu.

Tämän lisäksi lisäksi toisen viikon A*-algoritmissa löytyi myös toinen ongelma: se saattaa mennä ohuiden, viistojen esteiden läpi. Jos este on koostuu solmuista jotka ovat muotoa (x, y), (x+1, y+1), (x+2, y+2) … (x+n, y+n) tai muotoa (x, y), (x+1, y-1), (x+2, y-2) … (x+n, y-n), niin koska algoritmi voi mennä ikään kuin viistosti esteiden kulmien yli, se voi hypätä kahden kulmikkain olevan estesolmun/-pikselin välistä. Eri tutkimissani lähdemateriaaleissa algoritmit käyttäytyvät hieman eri tavoin. Toisissa estesolmun kulman yli voidaan hypätä diagonaalisessa suunnassa (tai kulkea solmun kulmaa hipoen, jos reitillä tai sitä kulkevalla objektilla ei ole leveyttä), toisissa taas solmu kierretään kokonaan. Täytyy miettiä ja tarkastella kumpaan ratkaisuun päädyn algoritmien kanssa.

Muuten olen perjantaihin mennessä yrittänyt tutkia ja lukea JSP-algoritmista. Kurssimateriaalissa oleva alkuperäinen dokumentaatio algoritmista ei ole kaikkein helposti lähestyttävin, joten etsin myös muita lähteitä. Vastaan tuli myös erilaisia demonstraatioita A*-algoritmista, jotka saivat minut miettimään, olisiko kuitenkin parempi kuvata solmuja ja karttaa jolloin muulla tavalla kuin matriisina. Oma algoritmi tuntuu epäsiistiltä vaikkei sillä ole välttämättä merkitystä, kunhan se toimii niin kuin pitää.

Varsinainen viikon ohjelmointityö on kuitenkin perjantaihin mennessä edennyt heikosti. Visuaalisten demostrointien myötä olen kuitenkin mielestäni ainakin pääpiirteittäin ymmärtänyt, mistä JPS-algoritmissa on kysymys ja miten sen tulisi toimia.

Albertan yliopiston tietojenkäsittelytieteen professorin Nathan Sturtevantin Youtube-kanavalta löytyi hyviä havainnollistavia videoita reitinhakualgoritmien toiminnasta, joita katsoin: 

 ![Single Agent Search Video 39: Canonical Orderings on Grids, Sturtevant N., Youtube](https://www.youtube.com/watch?v=rskXf8kO5Lw)
 ![Single Agent Search Video 40: Jump Point Search and Other Algorithms Using Canonical Orderings, Sturtevant N., Youtube](https://www.youtube.com/watch?v=__ZLnTwYNPk)
 
 Lisäksi löysin erilaisia nettiartikkeleita:

![A Visual Explanation of Jump Point Search, Nathan Witmer](https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html)
![Jump Point Search: Fast A* Pathfinding for Uniform Cost Grids, Albert Hofkamp](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)
![Implementation of A*, Amit Patel](https://www.redblobgames.com/pathfinding/a-star/implementation.html)

Lisäksi oli vielä tämä kurssimateriaalista löytyvä Daniel Haraborin ja Alban Grastienin artikkeli ![Online Graph Pruning for Pathfinding on Grid Maps](https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)

Lisäilen näitä linkkejä ja lähteitä vielä täsmällisemmin esitettynä ja muotoiltuna toteutusdokumenttiin.

Lauantaina olen jatkanut JPS:n tutkimista ja aloitettua sen tekoa funktioista, joilla haetaan matriisista/verkosta jump pointeja. JPS:n tekeminen on siis aluillaan, mutta mitään valmista testattavaa ja visualisoitavaa en ole vielä saanut valmiiksi. Lauantain puolella en ehtine saamaan JPS:ää testauskuntoon, joten täytyy jatkaa sen parissa työskentelyä huomenna tai viimeistään ensiviikolla. Siinä mielessä tämä viikko ehkä jäi hieman tavoitteista, mutta alkuun on päästy ja työ jatkuu.

Ensiviikolla siis tavoitteena saada JPS toimintakuntoon ja paikkailla A*:n puutteita, niin että A*:n ja JPS:n reittinhakuperiaatteet ovat samat (hypätäänkö kulmien yli vai ei).

Sunnuntaina 27. päivä tein testikokeiluitani ehkä 2,5 h ajan. Torstaina vilkuilin ja koitin tutustustua JPS-materiaaliin ehkä puolen tunnin verran, perjantaina tämä jatkui noin 4 tunnilla ja lauantaina ensimmäisten JPS-funktioiden tekoon ja raportteihin kului suunnilleen 4 h, joten sanoisin, että viikon työmäärä on ollut noin 11 tuntia, mikä jää hieman tavoiteajasta, mutta pitää koittaa jatkossa varata tarpeeksi aikaa ja kiriä työn osalta. Viimeistään pääsiäisloma antanee hieman tasoitteluaikaa.
