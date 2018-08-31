# Käyttöohje

Sovellus löytyy osoitteesta https://karaokepal.herokuapp.com/ .

## Pääsivu

Käyttäjä joka ei ole kirjautunut palveluun näkee pääsivun näkymässä linkit laulujen listaukseen, tilastoihin sekä kirjautumis- ja rekisteröintisivuille. Nämä toiminnot ovat siis käytössä ilman rekisteröintiä ja kirjautumista. Jos peruskäyttäjä on kirjautunut, näkee hän lisäksi pääsivulta laulun lisäystoiminnon, sekä linkin josta pääsee omaan laululistaan. Admin näkee näiden toimintojen lisäksi myös linkin adminin työkaluihin.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/startmenu.jpg" width="600">

## Rekisteröityminen

Rekisteröitymiseen pääsee oikean yläkulman linkistä "Create a new account". Lomakkeeseen syötetään nimi, käyttäjätunnus ja salasana. Jos käyttäjätunnus on jo käytössä, lomake ilmoittaa siitä virheviestillä. Tämä rekisteröityminen luo peruskäyttäjätilin.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/register.jpg" width="600">

## Kirjautuminen

Kun käyttäjätunnus on luotu, voi sovellukseen kirjautua kirjautumissivun kautta, jonne pääsee linkistä "Login".

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/login.jpg" width="600">

## Kaikkien tietokannan laulujen listaus

Jos käyttäjä on kirjautunut, näytetään kuvan mukainen laululistaus, muuten listataan ainoastaan laulun nimet. Laulun nimen perässä on linkki, josta pääsee tarkastelemaan laulun tietoja tarkemmin, sekä muokkaamaan laulun nimeä ja kuvausta. Add to my list- napista laulun voi valita omaan laululistaan ja delete napista (joka löytyy vain pääkäyttäjän näkymässä) voi poistaa laulun kokonaan tietokannasta.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/songlist.jpg" width="600">

## Laulun lisääminen tietokantaan

Kirjautunut käyttäjä voi lisätä lauluja tietokantaan. Lisäyslomakkeelle kirjoitetaan laulun nimi, vapaaehtoinen kuvaus ja artisti. Lomake tarkistaa onko löytyykö laulu jo lomakkeelle merkityllä artistilla. Samaa laulua ei lisätä uudelleen, joten tässä tilanteessa tulee virheilmoitus. Myös artistista tehdään tarkistus, niin ettei samaa artistia lisätä useaan kertaan.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/addsong.jpg" width="600">

## Laulun tarkastelu ja muuttaminen

Kun laululistasta valitaan jonkin laulun kohdalta linkki "Show", näytetään sivu, jolla on kerrottu laulun nimi, artisti ja kuvaus. Samalta sivulta nimeä ja kuvausta pääsee myös muokkaamaan täyttämällä halutut tiedot kenttiin ja painamalla "Save changes".

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/show.jpg" width="600">

## Omien laulujen listaus

Kirjautunut käyttäjä pääsee linkistä "Your songs" listaukseen, jossa listataan kaikki käyttäjän itselleen valitsemat laulut. Lauluja pääsee lisäämään listalle "List all songs" linkin kautta löytyvästä näkymästä. Omaan listaan voi merkitä kunkin laulun laulukertoja napista "Sing it!"

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/mylist.jpg" width="600">

## Tilastotiedot

Kaikki käyttäjät pääsevät etusivulta linkistä "Statistic" löytyvään tilastotietolistaukseen. Tilastosivulta näkyy listaus lauluista, joita käyttäjät ovat valinneet, sekä lukumäärä kuinka monelta käyttäjältä laulu löytyy.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/stats.jpg" width="600">

## Adminin työkalut

Jos käyttäjällä on adminoikeudet, näkyy hänelle yläpalkissa linkki "Admin tools". Linkin takaa näkyy listaus sovelluksen käyttäjistä ja heidän käyttäjätunnuksistaan. Tässä näkymässä voi muuttaa käyttäjien käyttäjäroolia, tai valita käyttäjän jonka tietoja halutaan muuttaa.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/admintools.jpg" width="600">

## Käyttäjän tietojen muutos

Käyttäjän nimeä ja salasanaa on mahdollista muokata kirjoittamalla halutut tiedot lomakkeelle ja painamalla "Save changes".

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/changeuser.jpg" width="600">






