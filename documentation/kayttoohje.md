# Käyttöohje

Sovellus löytyy osoitteesta https://karaokepal.herokuapp.com/ .

## Pääsivu

Käyttäjä joka ei ole kirjautunut palveluun näkee pääsivun näkymässä linkit laulujen listaukseen, tilastoihin sekä kirjautumis- ja rekisteröintisivuille. Nämä toiminnot ovat siis käytössä ilman rekisteröintiä ja kirjautumista. Jos peruskäyttäjä on kirjautunut, näkee hän lisäksi pääsivulta laulun lisäystoiminnon, sekä linkin josta pääsee omaan laululistaan. Admin näkee näiden toimintojen lisäksi myös linkin adminin työkaluihin.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/startmenu.jpg" width="400">

## Rekisteröityminen

Rekisteröitymiseen pääsee oikean yläkulman linkistä "Create a new account". Lomakkeeseen syötetään nimi, käyttäjätunnus ja salasana. Jos käyttäjätunnus on jo käytössä, lomake ilmoittaa siitä virheviestillä. Tämä rekisteröityminen luo peruskäyttäjätilin.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/register.jpg" width="400">

## Kirjautuminen

Kun käyttäjätunnus on luotu, voi sovellukseen kirjautua kirjautumissivun kautta, jonne pääsee linkistä "Login".

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/login.jpg" width="400">

## Kaikkien tietokannan laulujen listaus

Jos käyttäjä on kirjautunut, näytetään kuvan mukainen laululistaus, muuten listataan ainoastaan laulun nimet. Laulun nimen perässä on linkki, josta pääsee tarkastelemaan laulun tietoja tarkemmin, sekä muokkaamaan laulun nimeä ja kuvausta. Choose- napista laulun voi valita omaan laululistaan ja delete napista voi poistaa laulun kokonaan tietokannasta.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/login.jpg" width="400">

## Laulun lisääminen tietokantaan

Kirjautunut käyttäjä voi lisätä lauluja tietokantaan. Lisäyslomakkeelle kirjoitetaan laulun nimi, vapaaehtoinen kuvaus ja artisti. Lomake tarkistaa onko laulun nimi jo tietokannassa, samannimistä laulua ei lisätä uudelleen, vaan tässä tilanteessa tulee virheilmoitus. Myös artistista tehdään tarkistus, niin ettei samaa artistia lisätä useaan kertaan.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/addsong.jpg" width="400">

## Laulun tarkastelu ja muuttaminen

Kun laululistasta valitaan jonkin laulun kohdalta linkki "Show", näytetään sivu, jolla on kerrottu laulun nimi, artisti ja kuvaus. Samalta sivulta nimeä ja kuvausta pääsee myös muokkaamaan täyttämällä halutut tiedot kenttiin ja painamalla "Save changes".

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/show.jpg" width="400">

## Omien laulujen listaus

Kirjautunut käyttäjä pääsee linkistä "Your songs" listaukseen, jossa listataan kaikki käyttäjän itselleen valitsemat laulut. Lauluja pääsee lisäämään listalle "List all songs" linkin kautta löytyvästä näkymästä.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/mylist.jpg" width="400">

## Tilastotiedot

Kaikki käyttäjät pääsevät etusivulta linkistä "Statistic" löytyvään tilastotietolistaukseen. Tällä hetkellä tilastosivulta näkyy listaus lauluista, joita käyttäjät ovat valinneet, sekä lukumäärä kuinka monelta käyttäjältä laulu löytyy.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/stats.jpg" width="400">

## Adminin työkalut

Jos käyttäjällä on adminoikeudet, näkyy hänelle yläpalkissa linkki "Admin tools". Tällä hetkellä tämän linkin takaa näkyy listaus sovelluksen käyttäjistä ja heidän käyttäjätunnuksistaan.

<img src="https://github.com/apndx/Karaokepal/blob/master/documentation/admintools.jpg" width="400">

