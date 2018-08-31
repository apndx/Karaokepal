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

Projektin toteutus tehtiin hyvin kiireisellä aikataululla, käytännössä aikaa oli yhteensä kuusi viikkoa. Jo alussa pyrin karsimaan toteutuksen tietokantatauluja ja toimintoja, ja miettimään ohjelmastani mahdollisimman yksinkertaisen. Käytännössä kuitenkin selvisi, että myös osa näistä toiminnoista tulisi karsiutumaan lopulta pois käytettävissä olevan ajan rajallisuuden vuoksi. Itselläni meni myös paljon aikaa uusien asioiden omaksumiseen ja kokonaisuuden hahmottamiseen.

Yllämainituista toiminnallisuuksista jäi toteuttamatta laulun poistaminen käyttäjän listalta. Myös käyttötapauksiin merkityt hakutoiminnallisuudet jäivät haaveeksi.

Ohjelmassa on kuitenkin toimiva runko, ja sitä on helppo halutessaan laajentaa ja kehittää eteenpäin. Projektin edetessä oli myös palkitsevaa huomata, että ohjesivujen tuijottelun sijaan pystyi jo jossain määrin itse päättelemään, miten uusia toiminnallisuuksia voisi toteuttaa.

## Sovelluksen rajoitteet

Tällä hetkellä laulun nimen muokkaaminen jälkikäteen mahdollistaa nimen vaihtamisen sellaiseen laulunnimen ja artistin yhdistelmään, joka jo löytyy tietokannasta. Laulun lisäystoiminnolla tällaisten yhdistelmien lisääminen ei ole mahdollista.

## Sovelluksen puuttuvat ominaisuudet 

### Tiedon haku ja näyttäminen

Sovelluksessa ei ole hakutoiminnallisuuksia, vaan kaikki tieto esitetään listauksina. Tämä muodostuu pian ongelmaksi tietomäärien kasvaessa. Myös listausten sivutus olisi hyvä lisäominaisuus. Lisäksi olisi hyödyllistä, että listauksia voisi tehdä erilaisilla kriteereillä. Laulujen kuvauksissa kuvauksiin lisätyt linkit voisivat myös toimia linkkeinä, tällä hetkellä ne näkyvät vain tekstinä.

### Artisti

Tällä hetkellä artisti -taulun käsittely ohjelmassa on hyvin suppeaa, se on käytössä pelkästää laulun lisätietona. Hyviä lisäominaisuuksia olisi artistin kuvauksen näyttäminen. Tietokannan rakenteen puolesta olisi myös mahdollista, että laululla on useampi artisti, tätä ei kuitenkaan ole toistaiseksi ohjelmassa hyödynnetty.

### Käyttäjän tiedot

Tällä hetkellä käyttäjällä ei ole mahdollisuutta salasanansa muuttamiseen. Käyttäjän omien laujen listauksissa lauluissa voisi näkyä myös artisti, sekä käyttäjän käytössä olevat omat lisätiedot laulusta. Käyttäjän lauluihin ei ole myöskään vielä toteutettu sävellajitoiveen tallennusta.

### Ulkoasu

Projektissa pyrin keskittymään siihen, että olennaiset toiminnot toimivat mahdollisimman luotettavasti. Ulkoasun puolesta tyydyin toteuttamaan valmisratkaisun, ja varsinkin laulun muutossivun asettelu kaipaisi hiomista.
