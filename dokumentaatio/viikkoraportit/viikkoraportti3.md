# Viikkoraportti 3

Palasin sunnuntaina testailemaan toisen viikon aikaansaannosta eli A*-algoritmia. Testikattavuudessa algoritmista jäi kaksi if-haaraa tarkastamatta eli silloin, kun if-lauseiden ehto ei täyty. Kyseisissä haaroissa tarkastetaan, onko solmu jo lisätty kekoon ja jos on, se lisätään. Testitapauksissa ei siis käynyt niin, että jokin solmu olisi löytynyt jo keosta.

(Lisättävä kuva)

Yritin tehdä testitapauksia, jossa tämä haara tulisi läpikäydyksi. Tapaukssa, jossa tarkasteltava solmu on diagonaalisesti/kulmikkain nykyisen solmun, onnistuin luomaan sellaisen testimatriisin, että solmu löytyy jo keosta.

(Lisättävä kuva)

Tapaukseen, jossa nykysolmuun nähden sivuttain oleva solmu olisi jo keossa, en onnistunut luomaan testimatriisia, vaikka yritin tehdä  hirvittävän näköisiä sokkelomatriiseja, jotka yrittävät huijata algoritmia mahdollisimman paljon.

(Lisättävä kuva)

Rupesin tämän myötä miettimään toisen viikon A*-algoritmini ongelmia. Koska solmu talletetaan kekoon tuplena muodossa (f-arvo, (x, y)), if-lause ei tunnista solmua samaksi, mikäli verrattavan solmun f-arvo on eri kuin aiemmin lisätyn. Tämä mahdollistaa sen, että sama solmu lisätään kekoon useamman kerran, mikäli uudestaan lisättävälle solmulle on laskettu eri f-arvo kuin aiemmin. Mietin, miten ongelman kannattaisi ratkaista, koska solmut tulee nostaa keosta pienimmän f-arvon mukaan. Tallettaako keossa olevat solmut vaikka erilliseen hajautustauluun. Jos solmuja on paljon keossa, sen sisällön tarkastaminen on myös aikaa vievää.

Tämän lisäksi lisäksi toisen viikon A*-algoritmissa löytyi myös toinen ongelma: se saattaa mennä ohuiden, viistojen esteiden läpi. Jos este on koostuu solmuista jotka ovat muotoa (x, y), (x+1, y+1), (x+2, y+2) … (x+n, y+n) tai muotoa (x, y), (x+1, y-1), (x+2, y-2) … (x+n, y-n), niin koska algoritmi voi mennä ikään kuin viistosti esteiden kulmien yli, se voi hypätä kahden kulmikkain olevan estesolmun/-pikselin välistä. Eri materiaaleissa algoritmit käyttäytyvät hieman eri tavoin. Toisissa estesolmun kulman yli voidaan hypätä diagonaalisessa suunnassa (tai kulkea solmun kulmaa hipoen, jos reitillä tai sitä kulkevalla objektilla ei ole leveyttä), toisissa taas solmu kierretään kokonaan. Täytyy miettiä ja tarkastella kumpaan ratkaisuun päädyn algoritmien reitinhaussa.

Muuten olen perjantaihin mennessä yrittänyt tutkia ja lukea JSP-algoritmista. Kurssimateriaalissa oleva alkuperäinen dokumentaatio algoritmista ei ole kaikkein helposti lähestyttävin, joten etsin myös muita lähteitä. Vastaan tuli myös erilaisia demonstraatioita A*-algoritmista, jotka saivat minut miettimään, olisiko kuitenkin parempi kuvata solmuja ja karttaa jolloin muulla tavalla kuin matriisina. Oma algoritmi tuntuu sekavalta.

Varsinainen viikon ohjelmointityö on kuitenkin perjantaihin mennessä edennyt huonosti. Visuaalisten demostrointien myötä olen kuitenkin mielestäni ainakin pääpiirteittäin ymmärtänyt, mistä JPS-algoritmissa on kysymys ja miten sen tulisi toimia. 

(Linkkejä lähteistä yms. tähän)
