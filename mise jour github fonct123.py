# Créé par charl, le 27/02/2025 en Python 3.7

def est_bissextile(annee):
    """ Vérifie si une année est bissextile """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def lire_dates_depuis_fichier(nom_fichier):
    """ Lit un fichier contenant des dates et les retourne sous forme de liste """
    liste_dates = []
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne:
                try:
                    jour, mois, annee = map(int, ligne.split('/'))
                    liste_dates.append([jour, mois, annee])
                except ValueError:
                    print(f"Format incorrect dans le fichier : {ligne}")
    return liste_dates

def jour_de_la_semaine(date):
    """ Calcule le jour de la semaine pour une date donnée (Algorithme de Zeller modifié) """
    jour, mois, annee = date

    if mois < 3:  # Janvier et février sont traités comme mois 13 et 14 de l'année précédente
        mois += 12
        annee -= 1

    q = jour
    m = mois
    K = annee % 100
    J = annee // 100

    # Algorithme de Zeller
    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7

    jours_semaine = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    return jours_semaine[h]

if __name__ == "__main__":
    nom_fichier = "d:/NSI/project/date.txt"  # Chemin du fichier (mettre un chemin absolu si nécessaire)
    try:
        resultats = lire_dates_depuis_fichier(nom_fichier)
        for date in resultats:
            jour_semaine = jour_de_la_semaine(date)
            print("{:02}/{:02}/{} est un {}".format(date[0], date[1], date[2], jour_semaine))
    except FileNotFoundError:
        print("Fichier non trouvé. Vérifiez le chemin.")
