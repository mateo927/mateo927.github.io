SELECT*
FROM customers
WHERE country = 'Canada'
;

SELECT FirstName, LastName
FROM customers
WHERE country = 'France' AND city= 'Paris'
;

SELECT FirstName, LastName, Email
FROM customers
WHERE Email LIKE '%yahoo%'
;
SELECT FirstName, SupportRepid
FROM customers
WHERE SupportRepid = '3'
;
SELECT LastName,City
FROM employees
WHERE City = 'Calgary'
;
SELECT FirstName, LastName,Title
FROM employees
WHERE Title = 'Sales Support Agent'
;
SELECT FirstName, LastName, HireDate
FROM employees
WHERE HireDate > '2003%'
;
SELECT FirstName, LastName, Employeeid
FROM employees
WHERE Employeeid > '1'
;
SELECT*
FROM invoices
WHERE Invoiceid = '10'
;
SELECT *
FROM invoices
WHERE Total > '10'
;
SELECT *
FROM invoices
WHERE InvoiceDate = '2010'
;
SELECT * 
FROM invoices
WHERE BillingCity = 'USA'
;
SELECT *
FROM tracks
WHERE Milliseconds > '300000'
;
SELECT * 
FROM artists
WHERE Name LIKE '%The%'
;
SELECT * 
FROM artists
WHERE Name LIKE 'A%'
;
SELECT *
FROM albums
WHERE Title = 'Greatest Hits'
;


SELECT COUNT(*)
FROM invoices
;

SELECT SUM(total)
FROM invoices
;

SELECT AVG(total)
FROM invoices
;

SELECT MIN(total)
FROM invoices
;

SELECT MAX(total)
FROM invoices
;

select b.Name as artiste, a.Title
from  albums a
JOIN artists b ON b.ArtistId = a.ArtistId
Limit 5
;

select b.Name as artiste , a.Title
from  albums a
JOIN tracks b ON b.Albumid = a.Albumid
Limit 5
;

PRAGMA foreign_keys=ON;            /* SQLite seulement */
DROP TABLE IF EXISTS chien;        /* Supprimer la table chien si elle existe */
DROP TABLE IF EXISTS proprietaire; /* Supprimer la table proprietaire si elle existe */

-- Création de la table "proprietaire"
CREATE TABLE proprietaire (
    id_proprietaire INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    adresse VARCHAR(100),
    ville VARCHAR(50)
);

-- Insertion de quelques enregistrements dans la table "proprietaire"
INSERT INTO proprietaire (id_proprietaire, nom, prenom, adresse, ville)
VALUES
    (1, 'Dupont', 'Jean', '10 Rue de la Liberté', 'Vannes'),
    (2, 'Martin', 'Marie', '25 Avenue des Roses', 'Vannes'),
    (3, 'Leclerc', 'Pierre', '5 Rue du Port', 'Vannes'),
    (4, 'Dubois', 'Sophie', '30 Rue Saint-Goustan', 'Auray'),
    (5, 'Lefevre', NULL, '15 Avenue du Belvédère', 'Auray');

UPDATE proprietaire
SET prenom = 'TOM'
WHERE prenom is NULL;

UPDATE proprietaire
SET prenom = 'Aristide '
WHERE prenom is 'Jean' ;

-- vérification du contenu ded la table
select * from proprietaire;	
