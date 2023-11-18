# Gestionnaire de Bibliothèque

## Introduction

Ce projet est une application de gestion de bibliothèque développée en Python avec Tkinter pour l'interface graphique et MySQL pour la base de données. L'objectif est de moderniser le système de gestion manuelle de la bibliothèque de l'EPSI en automatisant les processus d'enregistrement des livres, de prêts, de retours et de suivi des utilisateurs.

## Fonctionnalités

- **Gestion des Livres :**
  - Ajout, suppression et modification des informations des livres (titre, auteur, genre, etc.).
  - Recherche des livres par différents critères (titre, auteur, ISBN).

- **Gestion des Utilisateurs :**
  - Enregistrement de nouveaux utilisateurs (étudiants, enseignants, etc.).
  - Gestion des informations des utilisateurs (nom, prénom, catégorie).

- **Prêt et Retour de Livres :**
  - Enregistrement des prêts de livres aux utilisateurs.
  - Suivi des retours et gestion des retards.

- **Interface Graphique :**
  - Création d'une interface utilisateur intuitive pour naviguer dans l'application.
  - Affichage des informations de manière claire et accessible.

- **Base de Données :**
  - Utilisation d'une base de données MySQL pour stocker les informations de manière persistante.
  - Mise en place de relations entre les données (ex. utilisateurs et prêts).

- **Rapports et Statistiques :**
  - Génération de rapports sur les prêts, les retards, les livres les plus populaires.
  - Analyse des tendances d'emprunt parmi les utilisateurs.

## Technologies Utilisées

- **Python 3** pour la logique principale.
- **Tkinter** pour l'interface graphique.
- **MySQL** pour la base de données.
- **MySQL Connector** pour la connexion Python-MySQL.

## Installation

### Prérequis

- Python 3 installé sur votre machine.
- Serveur MySQL opérationnel.

### Étapes d'Installation

1. **Clonez le Dépôt Git :**
   git clone https://github.com/SamirFezani/gestion-bibliotheque.git
   cd gestion-bibliotheque
Installez les Dépendances :

Copy code
pip install mysql-connector-python
Importez la Base de Données :

Exécutez le script SQL fourni dans le dossier sql : gestion_bibliotheque.sql.
Cela créera la base de données et les tables nécessaires.
Configurez la Connexion à la Base de Données :

Ouvrez le fichier main.py avec un éditeur de texte.
Modifiez les informations de connexion à la base de données (host, user, password, database) dans la section appropriée.
Utilisation
Exécutez l'Application :


Copy code
python main.py
Utilisez l'Interface Graphique :

Remplissez les champs pour ajouter un livre.
Sélectionnez un livre et utilisez les boutons pour effectuer des opérations d'emprunt et de retour.
Explorez les fonctionnalités d'ajout, de recherche et de gestion des utilisateurs.