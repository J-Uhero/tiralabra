# Testausdokumentti

Ohjelman testauksen jakaisin neljään eri kohtaan: yksikkötestaukseen pytest-kirjaston avulla, suorituskykytestaukseen, testaukseen kokeilemalla ohjelman toimintaa käytännössä ja koodin staattiseen analyysiin pylint-kirjaston avulla.

Yksikkötestaus testaa ohjelman keskeisintä toiminnallisuutta eli algoritmien toiminnan oikeellisuutta erilaisissa tapauksissa, myös kun algoritmi saa virheellisiä syötteitä. Yksikkötestit pystyy ajamaan komentoriviltä käsin "poetry run invoke tests" -komennolla. Yksikkötestien testikattavuus näyttää tältä:

![testikattavuusraportti](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/testikattavuusraportti-kaappaus2.png)

Käyttöliittymä ja visualisointi on jätetty yksikkötestien ulkopuolelle ja niitä on testattu käytännössä kokeilemalla. Niiden tehtävänä on mahdollistaa helppo algoritmien ajaminen ja näyttää karttakuvissa reitit ja käydyt solmut/jump pointit. Reitin visuaalisesta esitystavasta oli muutenkin hyötyä ohjelman testaamisessa, kun näki suoraan kartalta, millainen piirtynyt reitti on ja miten haku on edennyt.

Suorituskykytestauksessa olen ajanut A*:n ja JPS:n sekä pythagoran että esteettömän etäisyyden heuristiikoilla yhteensä yli tuhat kertaa kutakin algoritmia ja heuristiikkaa kohden satunnaisilla alku- ja päätepisteillä. Samalla olen tulostanut tietoja testin etenemisestä, käytetyistä alku- ja päätepisteistä ja ovatko ne ovat varmasti esteettömissä kohdissa sekä varmistanut, että A* ja JPS:n löytämä lyhin reitti on sama. Tämän avulla olen saanut sekä tietoa suorituskyvystä, että testattua algoritmin oikeaa toimintaa. Rajasin Manhattan-heuristiikan pois suorituskykytestauksesta, koska se ei saavuta aina lyhyintä etäisyyttä eikä ole vertailukelpoinen muiden heuristiikkojen kanssa. Manhattan-etäisyyttä voi kyllä ohjelmassa kokeilla, jos sen valitsee varta vasten asetuksista ajettavaksi heuristiikaksi.

Kaappaukset suorituskykytestauksesta:

![suorituskykytestaus2](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus1.png)

Tarkempi kuva saman kuvaajan lyhyistä etäisyyksistä:

![suorituskykytestaus2](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus2.png)
![suorituskykytestaus3](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus3.png)

Tarkempi kuva saman kuvaajan lyhyistä etäisyyksistä:

![suorituskykytestaus4](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus4.png)
![suorituskykytestaus5](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus5.png)
![suorituskykytestaus6](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus6.png)
![suorituskykytestaus7](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus7.png)
![suorituskykytestaus8](https://github.com/J-Uhero/tiralabra/blob/main/dokumentaatio/kuvat/suorituskykytestaus-kaappaus8.png)

Pylintin arvosana koodin siisteydestä ja asianmukaisuudesta on nyt 9,35. Jotkin asiat, jotka eivät ole menneet pylint-sääntöjen mukaan, ovat mielestäni perusteltuja algoritmien toiminnassa, kuten lyhyet muuttujien nimet ja hieman toisteinen koodi, koska algoritmin tehokas toiminta on pääasia.
