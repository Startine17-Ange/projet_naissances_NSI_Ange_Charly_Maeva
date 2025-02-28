# Créé par charl, le 27/02/2025 en Python 3.7

from datetime import datetime

def est_bissextile(annee):
    """ Vérifie si une année est bissextile. """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def date_valide(jour, mois, annee):
    """ Vérifie si une date est valide. """
    try:
        datetime(annee, mois, jour)  # Vérifie si la date est correcte
        return True
    except ValueError:
        return False

def lire_dates_depuis_fichier(nom_fichier):
    """ Lit un fichier contenant des dates et les retourne sous forme de liste. """
    liste_dates = []
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    try:
                        jour, mois, annee = map(int, ligne.split('/'))
                        if date_valide(jour, mois, annee):
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

    Entrée : date sous forme [jour, mois, année] (ex: [5, 3, 2024] pour le 5 mars 2024)
    Sortie : Nom du jour de la semaine ("Lundi", "Mardi", etc.)
    """
    jour, mois, annee = date
    date_obj = datetime(annee, mois, jour)
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return jours_semaine[date_obj.weekday()]

if __name__ == "__main__":
    nom_fichier = "d:/NSI/project/date.txt"  # Modifier le chemin selon ton fichier
    resultats = lire_dates_depuis_fichier(nom_fichier)

    if resultats:
        for date in resultats:
            jour_semaine = jour_de_la_semaine(date)
            print(f"{date[0]:02}/{date[1]:02}/{date[2]} est un {jour_semaine}")
    else:
        print("❌ Aucune date valide trouvée.")
