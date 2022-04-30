# Viikkoraportti 6

Tällä viikolla olen saanut JPS:n toimintakuntoon. Aikaa on kulunut varsin paljon debuggaukseen. Sen lisäksi olen toteuttanut kartan analysointia/muuttamista algoritmien ymmärtämäksi matriisiksi ja reitin visualisointia karttoihin, mikä oli tietysti keskeistä debuggauksen kannalta. Tällä hetkellä JPS:n visualisointi vaatii vielä hieman hiomista. Reitti lasketaan oikein ja oikeat jump pointit löydetään, mutta kulmasolmujen, joissa diagonaalihaku taittuu pysty- tai vaakahauksi vaatii vielä hiomista. Lisäksi algoritmit tarvitsevat vielä siistimistä, koska tiedostoihin on jäänyt debuggauksen käytettyjä ylimääräisiä funktioita ja toimintoja.

Maanantaina työstin kuvan analysoinnin ja matriisiksi muuttamisen parissa noin 3 h. Tiistaina jatkoin ja testailin algoritmien ajoa näillä matriiseilla ja reittikuvien luontia. Testailin käsin reitin piirtämistä ja huomasin, että välillä JPS-algoritmi löysi reitin, mutta välillä se näytti jäävän ikuiseen silmukkaan. Tästä alkoi debuggaaminen, jonka myötä aluksi sain korjattua algoritmin niin, ettei se jäänyt enää silmukkaan, mutta reitti ei välttämättä ollut oikea. Tämän jälkeen debuggaaminen jatkui yhteensä usean tunnin ajan, mitä varten tein erillaisia tulostuksia saadakseni kuvaa algoritmin toiminnasta. Aikaa käytin noin 8 h.

Torstaina sain viimein ratkaistua asian. Niin kuin voi olettaa, asia oli lopulta varsin pieni mutta merkittävä huolimattomuus: pääsilmukasta puuttui yksi rivi, jossa merkataan, mitkä solmut ovat jo käytä ainakin kertaalleen läpi. Näin ollen, jos samaan solmuun löytyi uusi reitti, tämä uusi reitti päivitettiin g-arvoihin, vaikka aiempi g-arvo olisikin jo löytynyt samalle solmulle. Aikaa käytin tällöin noin 2 h.

JPS-algoritmini toimii niin, että se tallentaa peräkkäiset solmut pääsilmukassa, jossa haetaan A*:n avulla lyhintä reittiä löydetyistä jump pointeista käsin, eikä reittiä analysoivassa hakufunktiossa. Näin ollen taittopisteet, joissa diagonaalihaku vaihtuu pysty- tai vaakahauksi jäävät tallentamatta tähän reittiin. Funktio, jossa lasken tämän reitin vaatii vielä hiomista tai sitten minun täytyy muuttaa algoritmia niin, että nämäkin solmut tallennetaan reittiin haun aikana, jotta saan tulostettua oikean reitin. Työskentelin tämän parissa perjantaina noin 2 h. Reitin pituus on tällä hetkellä laskettuna oikein molemmissa algoritmeissa, vaikka liukulukujen yhteen- ja kertolaskuissa voi tulla jotain hyvin pieniä poikkeamia, mitä liukulukujen kanssa voi tulla.

Latasin perjantaina myös vertaisarvioitavani työn ja jatkoin sen arvioimista lauantaina. Aikaa käytin yhteensä to-pe noin 2 h. Lisäksi lauantaina tein viikkoraportin ja päivitin myös a_starin testejä.

Viikon aikana työhön kului aikaa yhteensä noin 17,5 h.

Ensi viikolla tavoitteenani on tehdä ainakin käyttöliittymää, testausta ja siistimistä/hiomista.
