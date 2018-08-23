# Asennusohje

## Sovelluksen asennus Linux -koneelle Zip-tiedostosta

1. Sovelluksen käyttö omalla koneella vaatii Pythonia ja Sqlite3:sta. Varmista ensin että nämä löytyvät, ja asenna tarvittaessa. Kun lataat sovelluksesta ZIP-tiedoston, tulisi koneeltasi löytyä myös pakkauksen purkamiseen soveltuva ohjelma. 

2. Lataa sovelluksesta ZIP-pakattu tiedostot [Githubista](https://github.com/apndx/Karaokepal) -sivulta "Clone or download"-painikkeen kautta.

3. Pura tiedosto haluamaasi kansioon koneellasi.

4. Seuraavaksi tarvitse komentoriviä: avaa komentorivi kansioon, johon projektin pakkaus on purettu.

5. Pythonia varten tarvitaan virtuaaliympäristö. Se luodaan ja otetaan käyttöön näillä komennoilla:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

6. Seuraavaksi asennetaan sovelluksen käytössä oleva Flask-kirjasto:
```
$ pip install Flask
```

7. Sovelluksen riippuvuudet asennetaan requirements.txt -tiedostoon tällä komennolla:
```
$ pip install -r requirements.txt
```

8. Nyt sovellus on mahdollista käynnistää seuraavalla komennolla:
```
$ python run.py
```

9. Nyt pääset käyttämään sovellusta avaamalla selaimella osoitteen http://localhost:5000/


## Sovelluksen kloonaus

1. Kopioi [Github](https://github.com/apndx/Karaokepal) -sivulta "Clone or download" -painikkeen takaa löytyvä linkki.

2. Avaa komentorivi kansiossa, johon haluat projektin kloonin.

3. Kloonaa kansio, eli kopio projekti Githubista koneellesi:
```
$ git clone <github sivulta haettu linkki> <nimi kansiolle>
```
4. Seuraa paikallisen asennuksen ohjeiden kohdasta 3. eteenpäin.


## Sovelluksen asennus Herokuun

1. Sovellus tulisi ensin asentaa paikallisesti

2. Luo käyttäjätunnus Heroku -palveluun, jos sinulla ei vielä ole tunnusta.

3. Asenna koneellesi Herokun komentorivisovellus
```
$ sudo snap install heroku --classic
```

4. Kirjaudu Herokuun
```
$ heroku login

5. Siirry kansioon johon loit paikallisen projektin ja luo siitä Heroku projekti
```
$ cd ~/projekti
$ heroku create haluamasi_nimi_herokussa
```

6. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun
```
$ git remote add heroku
$ git add .
$ git commit -m "Heroku asennus"
$ git push heroku master
```
7. Projekti pyörii nyt Herokussa

8. Herokuun tarvitaan vielä PostgreSQL tietokanta, johon tiedot tallennetaan Herokussa
```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```

9. Sovellukseen pitää lisätä vielä käsin admin- tunnus, koska suoraan sovelluksessa on mahdollista lisätä 