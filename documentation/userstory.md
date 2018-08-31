# Käyttäjätarinoita

Tässä on listattu käyttäjätarinoita, ja niihin liittyviä SQL-kyselyitä. 


Peruskäyttäjänä

* Haluan selata tietokannasta löytyviä lauluja - Toteutettu
* Haluan saada listauksen valitsemistani lauluista - Toteutettu
* Haluan, että lauluja ja artisteja voi lisätä jos suosikkini ei ole vielä listalla mukana - Toteutettu
* Haluan pitää kirjaa siitä, kuinka monta kertaa lauluja on laulettu - Toteutettu
* Haluan voida tehdä listauksen lauluistani niin, että laulut on järjestetty sen mukaan, mitä on laulettu eniten tai vähiten - Toteutettu

* Haluan pystyä etsimään lauluja karaokelistaani sekä nimen, artistin että suosituimpien laulujen perusteella - Kesken


Pääkäyttäjänä

* Haluan pystyä hallinnoimaan tietokantaan tallennettuja käyttäjiä, ja muuttamaan tietoja tarvittaessa - Toteutettu


## Toimintoja jaoteltuna osa-alueittain

1. Tiedon selaaminen

Listaukset kaikista lauluista ja käyttäjistä tehdään aakkosjärjestyksessä nimen mukaan käyttäen valmiita Flaskin SQLAlchemyn query-metodeja. Samoin tehdään tarkistukset olemassaolevista lauluista ja artisteista, ettei niitä lisätessä synny duplikaatteja.


```Tiedon hakemisessa käytettyjä SQL-kyselyitä:


Kaikkien käyttäjien hakeminen käyttäjien nimen mukaan aakkosjärjestyksessä:

SELECT * FROM Account ORDER BY account.name;


Kaikkien laulujen hakeminen laulun nimen mukaan aakkosjärjestyksessä:

SELECT * from Song ORDER BY song.songname;


Listaus käyttäjän omista lauluista järjestettynä laulamiskertojen mukaan:

SELECT Song.id, Song.songname, Accountsongs.count, Song.description 
		FROM Song, Accountsongs
                WHERE Song.id = Accountsongs.song_id
                AND Accountsongs.account_id = ?
                ORDER BY Accountsongs.count DESC (?=<parametrinä annettu account.id>


Laululle etsitään artisti:

SELECT Artist.id 
		FROM Artist
                LEFT JOIN artistsongs ON Artist.id = artistsongs.artist_id 
                LEFT JOIN Song ON Song.id = artistsongs.song_id
                WHERE Song.id = ? (?=<parametrinä annettu song.id>)


Kuinka monella käyttäjällä on valittuna laulu. Laulusta ja artistista haetaan nimi, listaus on suosituimmuusjärjestyksessä:

SELECT Song.songname, Artist.artistname, 
		COUNT(DISTINCT account.id)
		FROM Song
		LEFT JOIN Accountsongs ON Song.id = accountsongs.song_id
		LEFT JOIN artistsongs ON artistsongs.song_id = Song.id
		LEFT JOIN Artist ON Artist.id = artistsongs.artist_id
		LEFT JOIN Account ON Account.id = accountsongs.account_id
		GROUP BY Song.songname, Artist.artistname
		ORDER BY COUNT(DISTINCT account.id) DESC


Listataan laulut niin, että tuloksessa löytyy laulun nimi ja artistin nimi, lista aakkosjärjestyksessä laulun nimen mukaan:

SELECT Song.id, Song.songname, Artist.artistname FROM Song
		LEFT JOIN artistsongs ON Song.id = artistsongs.song_id 
		LEFT JOIN Artist ON Artist.id = artistsongs.artist_id
		ORDER BY Song.songname


Tarkistetaan, onko tietokannassa jo tietty laulu yhdistettynä tiettyyn artistiin:

SELECT * FROM artistsongs
                WHERE artistsongs.artist_id = ?
                AND artistsongs.song_id = ? (?=<parametrinä annettut artist.id ja song.id> 


Tarkistetaan, onko kirjautuneella käyttäjällä jo tietty laulu:

SELECT * FROM Accountsongs
                WHERE accountsongs.account_id = ?
                AND accountsongs.song_id = ? (?=<parametrinä annettut account.id ja song.id> 

```

2. Tiedon lisääminen

Sovellukseen voi lisätä peruskäyttäjiä ja lauluja, tiedon lisäys ja lisäykseen liittyvät duplikaattitarkistukset tehdään käyttäen Flaskin SQLAlchemyn toimintoja.

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

Kaikki käyttäjät voivat poistaa tietokantaan lisättyjä lauluja laululistauksesta. Pääkäyttäjät voivat poistaa käyttäjiä. Tietojen poistoon käytetään Flaskista löytyviä ominaisuuksia.

``` Tiedon poistamista SQL:llä:

Poistetaan tietokannasta laulu:

DELETE FROM Song WHERE song.id = ?; (? = <parametrinä annettu song.id >)

```

5. Kirjautuminen

Käyttäjät voivat kirjautua sovellukseen. Sovelluksen näkymä muuttuu sen mukaan, onko kirjauduttu ollenkaan, tai onko kirjautuja admin vai peruskäyttäjä. Kirjautuminen on toteutettu Flaskin ominaisuuksilla. Toiminnot on myös autorisoitu niin, että niihin ei pääse käsiksi myöskään suorasta osoitteesta ilman oikean tyyppistä kirjautumista.


## Tietokantataulut

Tilastosivulla käytettävissä tiedoissa on tietokanna indeksointi (laulun nimi, artistin nimi)
Tauluihin on toteutettu toimintoja seuraavasti (Create, Read, Update, Delete):

Song - CRUD
Artist - CR
Account - CRUD
Accountsong - CU (näistä saa myös listauksen käyttäjäkohtaisesti)
Artistsong - CRD (poisto tapahtuu song poiston yhteydessä)

## Luotilauseet

CREATE TABLE song (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	songname VARCHAR(144) NOT NULL, 
	description VARCHAR(1000), 
	PRIMARY KEY (id)
);

CREATE INDEX ix_song_songname ON song (songname);

CREATE TABLE artist (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	artistname VARCHAR(144) NOT NULL, 
	description VARCHAR(1000), 
	PRIMARY KEY (id)
);

CREATE INDEX ix_artist_artistname ON artist (artistname);

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	user_role VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);

CREATE TABLE accountsongs (
	account_id INTEGER NOT NULL, 
	song_id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	modulation INTEGER NOT NULL, 
	count INTEGER NOT NULL, 
	owndescription VARCHAR(1000), 
	PRIMARY KEY (account_id, song_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(song_id) REFERENCES song (id)
);

CREATE TABLE artistsongs (
	song_id INTEGER NOT NULL, 
	artist_id INTEGER NOT NULL, 
	PRIMARY KEY (song_id, artist_id), 
	FOREIGN KEY(song_id) REFERENCES song (id), 
	FOREIGN KEY(artist_id) REFERENCES artist (id)
);





