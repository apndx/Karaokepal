# Karaokepal


Tämä on harjoitustyö tietokantasovelluskurssille.

Tarkoituksena on laatia ohjelma, josta löytyy listauksia karaokekappaleista. 

Ohjelmalla on peruskäyttäjiä ja pääkäyttäjiä, pääkäyttäjillä on täydet oikeudet ohjelmaan ja peruskäyttäjillä on joitakin rajoituksia.

Palveluun voi lisätä artisteja ja lauluja. Lauluihin voi lisätä kuvauksen ja linkin, jonka takaa löytyy lisätietona esimerkiksi sanat, äänite tai video.

Pääsivulta löytyy listaus lauluista aakkosjärjestyksessä, lauluista pääsee myös kunkin laulun kohdalta lisätietosivulle. Tilastosivulla löytyy listaus kaikista lauluista suosituimmuusjärjestyksessä.

Käyttäjät voivat luoda oman listauksen suosikkilauluistaan, omaan listaan voi lisätä lauluja pääsivun laululistasta. Omaan listaan voi merkitä kun on käynyt laulamassa jotain, ja tästä koostuu tilastotietoa siitä montako kertaa kutakin laulua on laulettu. 

## Toimintoja:

### Käyttäjätunnus ja kirjautuminen

* Käyttäjän luominen
* Kirjautuminen - toiminnot muuttuvat sen mukaan onko kirjautunut ollenkaan, ja onko pääkäyttäjä vai tavallinen käyttäjä

### Laulutietokanta

* Laulujen listaus - pääsivun lista aakkosjärjestyksessä, tilastosivulla suosituimmuusjärjestyksessä
* Laulujen lisäys - artisti lisätään samalla jos sitä ei vielä löydy
* Laulun tietojen muuttaminen - muokkaustoimintoon pääsee pääsivun laululistasta
* Laulun poistaminen - tämä toiminto on näkyvissä vain pääkäyttäjälle pääsivun laululistasta

### Käyttäjäkohtaiset ominaisuudet

* Laulun lisäys käyttäjän listaan - käyttäjä voi lisätä laulun listaansa pääsivulta
* Omien laulujen listaus - omaan listaan pääsee yläpalkin oikean reunan linkistä
* Laulukerran merkitseminen - omassa listassa voi pitää kirjaa laulukerroista, omat laulut on järjestetty suosituimmuusjärjestykseen
* Admin-tunnuksilla löytyy mahdollisuus muuttaa käyttäjän nimeä ja salasanaa

## Linkit sovellukseen ja dokumentaatioon

* [Sovellus Herokussa](https://karaokepal.herokuapp.com/)
* [Tietokantakaavio](https://github.com/apndx/Karaokepal/blob/master/documentation/tietokantakaavio.png)
* [Userstories](https://github.com/apndx/Karaokepal/blob/master/documentation/userstory.md)
* [Asennusohje](https://github.com/apndx/Karaokepal/blob/master/documentation/asennusohje.md)
* [Käyttöohje](https://github.com/apndx/Karaokepal/blob/master/documentation/kayttoohje.md)
* [Pohdintaa projektista](https://github.com/apndx/Karaokepal/blob/master/documentation/reflektio.md)

## Testikäyttäjät

### Tavallinen käyttäjä (basicuser)

* Username: elvis
* Password: test
* Name: Test Elvis

### Adminkäyttäjä (admin)

* Username: sitrus	
* Password: sitrus	
* Name: Sitruuna

