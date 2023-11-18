import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connexion à la base de données
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="gestionbibliotheque"
)

# Initialisation du curseur avec un gestionnaire de contexte
with db_connection.cursor() as cursor:

    # Définition de la classe Livre
    class Livre:
        def __init__(self, clef_livre, titre, auteur, isbn, disponible):
            self.clef_livre = clef_livre
            self.titre = titre
            self.auteur = auteur
            self.isbn = isbn
            self.disponible = disponible

    livres = []  # Ajout de la liste livres pour stocker les objets Livre

    # Fonction pour insérer un livre dans la base de données
    def inserer_livre(livre):
        cursor.execute("INSERT INTO tblLivre (Titre, Auteur, ISBN, Disponible) VALUES (%s, %s, %s, %s)",
                       (livre.titre, livre.auteur, livre.isbn, 1))
        db_connection.commit()

    # Fonction pour emprunter un livre dans la base de données
    def emprunter_livre_db(isbn):
        cursor.execute("UPDATE tblLivre SET Disponible = 0 WHERE ISBN = %s", (isbn,))
        db_connection.commit()

    # Fonction pour retourner un livre dans la base de données
    def retourner_livre_db(isbn):
        cursor.execute("UPDATE tblLivre SET Disponible = 1 WHERE ISBN = %s", (isbn,))
        db_connection.commit()

    # Fonction pour récupérer les livres depuis la base de données
    def recuperer_livres():
        livres_listbox.delete(0, tk.END)  # Efface la liste actuelle
        cursor.execute("SELECT ClefLivre, Titre, Auteur, ISBN, Disponible FROM tblLivre")
        result = cursor.fetchall()
        for row in result:
            clef_livre, titre, auteur, isbn, disponible = row
            livre = Livre(clef_livre, titre, auteur, isbn, disponible)
            livres.append(livre)
            livres_listbox.insert(tk.END, f"{titre} par {auteur}, ISBN: {isbn}, Disponible: {livre.disponible}")

    # Fonction pour ajouter un livre
    def ajouter_livre():
        titre = titre_entry.get()
        auteur = auteur_entry.get()
        isbn = isbn_entry.get()

        if titre and auteur and isbn:
            livre = Livre(None, titre, auteur, isbn, True)
            inserer_livre(livre)
            livres.append(livre)  # Ajout du livre à la liste
            livres_listbox.insert(tk.END, f"{titre} par {auteur}, ISBN: {isbn}, Disponible: {livre.disponible}")
            titre_entry.delete(0, tk.END)
            auteur_entry.delete(0, tk.END)
            isbn_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")

    # Fonction pour emprunter un livre
    def emprunter_livre():
        selected_livre = livres_listbox.curselection()
        if selected_livre:
            index = selected_livre[0]
            livre = livres[index]
            if livre.disponible:
                emprunter_livre_db(livre.isbn)
                livres_listbox.delete(index)
                livres_listbox.insert(index, f"{livre.titre} par {livre.auteur}, ISBN: {livre.isbn}, Disponible: Non")
            else:
                messagebox.showinfo("Déjà emprunté", "Le livre est déjà emprunté.")
        else:
            messagebox.showwarning("Sélection manquante", "Veuillez sélectionner un livre.")

    # Fonction pour retourner un livre
    def retourner_livre():
        selected_livre = livres_listbox.curselection()
        if selected_livre:
            index = selected_livre[0]
            livre = livres[index]
            if not livre.disponible:
                retourner_livre_db(livre.isbn)
                livres_listbox.delete(index)
                livres_listbox.insert(index, f"{livre.titre} par {livre.auteur}, ISBN: {livre.isbn}, Disponible: Oui")
            else:
                messagebox.showinfo("Déjà disponible", "Le livre est déjà disponible.")
        else:
            messagebox.showwarning("Sélection manquante", "Veuillez sélectionner un livre.")

    # Fenêtre principale
    root = tk.Tk()
    root.title("Gestionnaire de Bibliothèque")

    # Widgets
    titre_label = tk.Label(root, text="Titre:")
    titre_label.pack()

    titre_entry = tk.Entry(root, width=50)
    titre_entry.pack()

    auteur_label = tk.Label(root, text="Auteur:")
    auteur_label.pack()

    auteur_entry = tk.Entry(root, width=50)
    auteur_entry.pack()

    isbn_label = tk.Label(root, text="ISBN:")
    isbn_label.pack()

    isbn_entry = tk.Entry(root, width=50)
    isbn_entry.pack()

    ajouter_button = tk.Button(root, text="Ajouter le livre", command=ajouter_livre)
    ajouter_button.pack(pady=10)

    livres_listbox = tk.Listbox(root, height=15, width=100)
    livres_listbox.pack(pady=10)

    recuperer_livres()  # Charge les livres existants lors du démarrage de l'application

    emprunter_button = tk.Button(root, text="Emprunter le livre", command=emprunter_livre)
    emprunter_button.pack(pady=5)

    retourner_button = tk.Button(root, text="Retourner le livre", command=retourner_livre)
    retourner_button.pack(pady=5)

    root.mainloop()
