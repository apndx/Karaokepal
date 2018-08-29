# Käyttäjätarinoita

Tässä on listattu käyttäjätarinoita, ja niihin liittyviä SQL-kyselyitä. 


Peruskäyttäjänä

* Haluan selata tietokannasta löytyviä lauluja - Toteutettu
* Haluan saada listauksen valitsemistani lauluista - Toteutettu
* Haluan, että lauluja ja artisteja voi lisätä jos suosikkini ei ole vielä listalla mukana - Toteutettu

* Haluan pystyä etsimään lauluja karaokelistaani sekä nimen, artistin että suosituimpien laulujen perusteella - Kesken
* Haluan nähdä tilastotietoja lauluista, joita olen laulanut - Kesken
* Haluan voida tehdä listauksen lauluistani niin, että laulut on järjestetty sen mukaan, mitä on laulettu eniten tai vähiten - Kesken


Pääkäyttäjänä

* Haluan pystyä hallinnoimaan tietokantaan tallennettuja käyttäjiä, ja muuttamaan tietoja tarvittaessa - Toteutettu


## Toimintoja jaoteltuna osa-alueittain

1. Tiedon selaaminen

Listaukset kaikista lauluista ja käyttäjistä tehdään aakkosjärjestyksessä nimen mukaan käyttäen valmiita query-metodeja.
Samoin tehdään tarkistukset olemassaolevista lauluista ja artisteista.



```Tiedon hakemisessa käytettyjä SQL-kyselyitä:


Kaikkien käyttäjien hakeminen käyttäjien nimen mukaan aakkosjärjestyksessä:

SELECT * FROM Account ORDER BY account.name;


Kaikkien laulujen hakeminen laulun nimen mukaan aakkosjärjestyksessä:

SELECT * from Song ORDER BY song.songname;


Listaus käyttäjän omista lauluista aakkosjärjestyksessä laulun nimen mukaan:

SELECT Song.songname, Song.description FROM Song
                      LEFT JOIN accountsongs ON Song.id = accountsongs.song_id
                      WHERE accountsongs.account_id = ?
                      ORDER BY Song.songname (? = <parametrinä annettu current_user.id>) 


Laululle etsitään artisti:

SELECT Artist.id FROM Artist
                      LEFT JOIN artistsongs ON Artist.id = artistsongs.artist_id 
                      LEFT JOIN Song ON Song.id = artistsongs.song_id
                      WHERE Song.id = ? (?=<parametrinä annettu song.id>)


Kuinka monella käyttäjällä on valittuna laulu, listaus suosituimmuusjärjestyksessä:

SELECT Song.songname, COUNT(accountsongs.song_id) AS howmany FROM Song 
		      LEFT JOIN accountsongs ON  Song.id = accountsongs.song_id 
		      LEFT JOIN Account ON Account.id = accountsongs.account_id 
		      GROUP BY Song.songname  ORDER BY howmany DESC;

```

2. Tiedon lisääminen

Sovellukseen voi lisätä peruskäyttäjiä ja lauluja, tiedon lisäys ja lisäykseen liittyvät duplikaattitarkistukset tehdään käyttäen Flaskin toimintoja.

Kun sovellus on otettu käyttöön ja käynnistetty ensimmäisen kerran, tulisi siihen lisätä admin -käyttäjä suoraan tietokantaan (nimi, tunnus ja salasana- kohtiin täytetään halutut tiedot):


``` Tiedon lisäämistä SQL:llä:

Adminin lisäys:
INSERT INTO account (name, username, password, user_role) VALUES ('nimi', 'tunnus', 'salasana', 'admin');

```

3. Tiedon muokkaaminen 

Kaikki käyttäjät voivat muokata laulujen nimeä ja kuvausta. Pääkäyttäjät voivat muokata käyttäjien tietoja.
Tietojen muokkauksessa käytetään jälleen Flaskista löytyviä ominaisuuksia.

``` Tiedon muokkausta SQL:llä:

Muutetaan laulun nimeä ja kuvausta:

UPDATE Song SET songname = '?', description = '?' 
			WHERE song.id = ?; (? = <parametrinä annettu erikseen nimi, kuvaus ja song.id >)

```

4. Tiedon poistaminen

Kaikki käyttäjät voivat poistaa tietokantaan lisättyjä lauluja voi poistaa laululistauksesta. Pääkäyttäjät voivat poistaa käyttäjiä.
Tietojen poistoon käytetään Flaskista löytyviä ominaisuuksia.

``` Tiedon poistamista SQL:llä:

Poistetaan tietokannasta laulu:

DELETE FROM Song WHERE song.id = ?; (? = <parametrinä annettu song.id >)

```

5. Kirjautuminen

Käyttäjät voivat kirjautua sovellukseen. Sovelluksen näkymä muuttuu sen mukaan, onko kirjauduttu ollenkaan, tai onko kirjautuja admin vai peruskäyttäjä. Kirjautuminen on toteutettu Flaskin ominaisuuksilla.







