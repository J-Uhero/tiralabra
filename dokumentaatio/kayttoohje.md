# Käyttöohje

Ohjelman riippuvuudet saa asennettua komennolla
```bash
poetry install
```

Ohjelma käynnistetään komennolla 
```bash
poetry run invoke start
```

Käynnistämisen jälkeen ohjelmaa operoidaan komentoriviltä. Valikossa navigointiin käytetään syötteenä numeroita valikon ohjeiden mukaan. 

Testien ajaminen:
```bash
poetry run invoke tests
```

Kattavuustestauksen ajaminen:
```bash
poetry run invoke coverage
```

Kattavuusraportin teko
```bash
poetry run invoke coverage-report
```

Koodin pylint-analyysi:
```bash
poetry run invoke lint
```


