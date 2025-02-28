# Créé par charl, le 28/02/2025 en Python 3.7


from datetime import datetime  # Importation du module datetime pour manipuler les dates

def est_bissextile(annee):
    """
    Vérifie si une année est bissextile.
    Une année est bissextile si :
    - Elle est divisible par 4 et non par 100, ou
    - Elle est divisible par 400.
    """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def date_valide(jour, mois, annee):
    """
    Vérifie si une date donnée est valide.

    Entrées :
    - jour : entier représentant le jour
    - mois : entier représentant le mois
    - annee : entier représentant l'année

    Sortie :
    - Retourne True si la date est valide, sinon False.
    """
    try:
        datetime(annee, mois, jour)  # Vérifie si la date peut être créée sans erreur
        return True
    except ValueError:
        return False

def lire_dates_depuis_fichier(nom_fichier):
    """
    Lit un fichier contenant des dates et retourne une liste des dates valides.

    Entrée :
    - nom_fichier : chaîne de caractères, chemin du fichier contenant les dates

    Sortie :
    - liste_dates : liste des dates valides sous forme [[jour, mois, année], ...]

    Affiche un message d'erreur si :
    - Le fichier est introuvable.
    - Une ligne a un format incorrect.
    - Une date est invalide.
    """
    liste_dates = []
    try:
        with open(nom_fichier, 'r') as fichier:  # Ouvre le fichier en lecture
            for ligne in fichier:
                ligne = ligne.strip()  # Supprime les espaces inutiles
                if ligne:  # Vérifie que la ligne n'est pas vide
                    try:
                        jour, mois, annee = map(int, ligne.split('/'))  # Convertit la ligne en trois entiers
                        if date_valide(jour, mois, annee):  # Vérifie si la date est valide
                            liste_dates.append([jour, mois, annee])
                        else:
                            print(f"❌ Date invalide ignorée : {ligne}")
                    except ValueError:
                        print(f"⚠️ Format incorrect ignoré : {ligne}")
    except FileNotFoundError:
        print("❌ Fichier non trouvé. Vérifiez le chemin.")
    return liste_dates

def jour_de_la_semaine(date):
    """
    Détermine le jour de la semaine d'une date donnée.

    Entrée :
    - date : liste [jour, mois, année] (ex: [5, 3, 2024] pour le 5 mars 2024)

    Sortie :
    - Nom du jour de la semaine sous forme de chaîne de caractères ("Lundi", "Mardi", etc.).
    """
    jour, mois, annee = date
    date_obj = datetime(annee, mois, jour)  # Création d'un objet datetime
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return jours_semaine[date_obj.weekday()]  # Retourne le jour correspondant

# Bloc principal : exécution du programme
if __name__ == "__main__":
    nom_fichier = "d:/NSI/project/date.txt"  # Modifier le chemin selon l'emplacement du fichier
    resultats = lire_dates_depuis_fichier(nom_fichier)  # Récupère la liste des dates valides

    if resultats:  # Vérifie s'il y a des dates valides
        for date in resultats:
            jour_semaine = jour_de_la_semaine(date)  # Détermine le jour de la semaine
            print(f"{date[0]:02}/{date[1]:02}/{date[2]} est un {jour_semaine}")
    else:
        print("❌ Aucune date valide trouvée.")  # Message si aucune date n'est valide

