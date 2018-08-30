# Suunnitelmat ja niiden toteutuminen

## Alkuperäinen suunnitelma 


>Tämä on harjoitustyö tietokantasovelluskurssille.
>
>Tarkoituksena on laatia ohjelma, josta löytyy listauksia karaokekappaleista. 
>
>Ohjelmalla on peruskäyttäjiä ja pääkäyttäjiä, pääkäyttäjillä on täydet oikeudet ohjelmaan ja peruskäyttäjillä on joitakin rajoituksia.
>
>Palveluun voi lisätä artisteja ja lauluja. Lauluihin voi lisätä kuvauksen ja linkin, jonka takaa löytyy lisätietona esimerkiksi sanat,   äänite tai video.
>
>Käyttäjät voivat selata tietokantaan lisättyjä lauluja, niitä voi hakea nimen tai artistin perusteella. Laulut voi myös hakea suosituimmuusjärjestykseen sen mukaan, kuinka monta kertaa käyttäjät ovat laulaneet jotain laulua.
>
>Käyttäjät voivat luoda oman listauksen suosikkilauluistaan. Omaan listaan voi merkitä kun on käynyt laulamassa jotain, ja tästä koostuu tilastotietoa siitä montako kertaa kutakin laulua on laulettu. Käyttäjä voi myös merkitä omaan listaansa laulusta kuvauksen, jota voi muutella tarpeen mukaan.
>
> ## Toimintoja:
>
>* Käyttäjän luominen
>* Käyttäjän poistaminen
>* Kirjautuminen
>* Laulun lisääminen
>* Laulun tietojen muuttaminen
>* Laulun poistaminen
>* Laulujen listaus
>* Artistin lisääminen
>* Laulun lisäys käyttäjän listaan
>* Laulukerran merkitseminen 
>* Laulun poisto käyttäjän listalta
>* Käyttäjän laululistan näyttäminen

## Toteutuminen

Projektin toteutus tehtiin hyvin kiireisellä aikataululla, käytännössä aikaa oli yhteensä kuusi viikkoa. Jo alussa pyrin karsimaan toteutuksen tietokantatauluja ja toimintoja, ja miettimään ohjelmastani mahdollisimman yksinkertaisen. Käytännössä kuitenkin selvisi, että myös osa näistä toiminnoista tulisi karsiutumaan lopulta pois käytettävissä olevan ajan rajallisuuden vuoksi.

Yllämainituista toiminnallisuuksista jäi toteuttamatta laulukerran merkitseminen ja laulun poistaminen käyttäjän listalta. Myös käyttötapauksiin merkityt hakutoiminnallisuudet jäivät haaveeksi.

Ohjelmassa on kuitenkin toimiva runko, ja sitä on helppo halutessaan laajentaa ja kehittää eteenpäin.

## Sovelluksen rajoitteet

Tällä hetkellä laulun nimen muokkaaminen jälkikäteen mahdollistaa nimen vaihtamisen sellaiseen laulunnimen ja artistin yhdistelmään, joka jo löytyy tietokannasta. Suoraan tällaisia lauluja ei voi lisätä useampia.

## Sovelluksen puuttuvat ominaisuudet 

Sovelluksessa ei ole hakutoiminnallisuuksia, vaan kaikki tieto esitetään listauksina. Tämä muodostuu pian ongelmaksi tietomäärien kasvaessa. Sivutus olisikin hyvä saada toimimaan. Lisäksi olisi hyödyllistä, että listauksia voisi tehdä erilaisilla kriteereillä. Tällä hetkellä artisti -taulun käsittely ohjelmassa on hyvin suppeaa, se on käytössä pelkästää laulun lisätietona. Tällä hetkellä käyttäjällä ei ole mahdollisuutta salasanansa muuttamiseen, se olisi hyvä lisätä. Laulujen kuvauksissa kuvauksiin lisätyt linkit voisivat myös toimia linkkeinä, nyt ne näkyvät vain tekstinä. Listauksissa olisi hyvä, että artististin nimet näkyisivät suoraan, nyt ne ovat lisätietolinkin takana.
