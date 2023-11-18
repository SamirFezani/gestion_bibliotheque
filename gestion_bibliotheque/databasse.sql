-- Créer la base de données
CREATE DATABASE IF NOT EXISTS GestionBibliotheque;

-- Utiliser la base de données
USE GestionBibliotheque;

-- Créer la table tblLivre
-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS GestionBibliotheque;

-- Utiliser la base de données
USE GestionBibliotheque;

-- Créer la table tblLivre si elle n'existe pas
CREATE TABLE IF NOT EXISTS tblLivre (
    ClefLivre INT AUTO_INCREMENT PRIMARY KEY,
    Titre VARCHAR(255) NOT NULL,
    Auteur VARCHAR(255) DEFAULT NULL,
    ISBN VARCHAR(50) DEFAULT NULL,
    Disponible BOOLEAN DEFAULT TRUE
);

-- Créer la table tblExemplaireLivre si elle n'existe pas
CREATE TABLE IF NOT EXISTS tblExemplaireLivre (
    ClefExemplaire INT AUTO_INCREMENT PRIMARY KEY,
    ClefLivre INT NOT NULL,
    FOREIGN KEY (ClefLivre) REFERENCES tblLivre(ClefLivre)
);


-- Ajouter des livres
INSERT INTO tblLivre (Titre, Auteur) VALUES 
    ('The Catcher in the Rye', 'J.D. Salinger'),
    ('To Kill a Mockingbird', 'Harper Lee'),
    ('The Hobbit', 'J.R.R. Tolkien'),
    ('The Great Gatsby', 'F. Scott Fitzgerald'),
    ('The Shining', 'Stephen King'),
    ('It', 'Stephen King'),
    ('Psycho', 'Robert Bloch'),
    ('The Exorcist', 'William Peter Blatty'),
    ('Frankenstein', 'Mary Shelley'),
    ('Dracula', 'Bram Stoker'),
    ('The Silence of the Lambs', 'Thomas Harris'),
    ('Carrie', 'Stephen King'),
    ('The War of the Worlds', 'H.G. Wells');

-- Vérifier si la colonne 'Genre' existe
SELECT COUNT(*) INTO @column_exists
FROM information_schema.columns
WHERE table_name = 'tblLivre' AND column_name = 'Genre';

-- Créer une procédure stockée pour ajouter la colonne 'Genre' si elle n'existe pas déjà
DELIMITER //
CREATE PROCEDURE AddGenreColumn()
BEGIN
    IF @column_exists = 0 THEN
        ALTER TABLE tblLivre
        ADD COLUMN Genre VARCHAR(50) DEFAULT NULL;
    END IF;
END //
DELIMITER ;

-- Appeler la procédure stockée
CALL AddGenreColumn();

-- Mettre à jour les genres des livres existants
UPDATE tblLivre
SET Genre = 'Roman'
WHERE ClefLivre IN (1, 2, 3, 4);

UPDATE tblLivre
SET Genre = 'Horreur'
WHERE ClefLivre IN (5, 6, 7, 8);
