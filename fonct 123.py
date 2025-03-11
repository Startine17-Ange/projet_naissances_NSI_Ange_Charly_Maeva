# Fonction pour vérifier si une année est bissextile
def est_bissextile(annee: int) -> bool:
    """Vérifie si une année est bissextile"""
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Fonction pour lire des dates depuis un fichier texte
def lire_dates_depuis_fichier(nom_fichier: str) -> list:
    """Lit un fichier contenant des dates et retourne une liste de dates"""
    li_dates = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()  # Lire toutes les lignes
    for ligne in lignes:
        ligne = ligne.strip()
        if ligne:
            jour, mois, annee = map(int, ligne.split('/'))
            li_dates.append([jour, mois, 2000 + annee])  # Ajouter à la liste
    return li_dates

# Fonction pour déterminer le jour de la semaine d'une date donnée
def jour_de_la_semaine(date: list) -> str:
    """Calcule le jour de la semaine en utilisant l'algorithme de Zeller"""
    jour, mois, annee = date
    if mois < 3:
        mois += 12
        annee -= 1
    h = (jour + (13 * (mois + 1)) // 5 + annee % 100 + (annee % 100 // 4) + (annee // 400) - (2 * (annee // 100))) % 7
    jours_semaine = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    return jours_semaine[h]

# Exécution du programme principal
if __name__ == "__main__":
    nom_fichier = "N:/NSI/project/date.txt"  # Chemin du fichier contenant les dates
    resultats = lire_dates_depuis_fichier(nom_fichier)

    # Afficher le jour de la semaine pour chaque date
    for date in resultats:
        jour_semaine = jour_de_la_semaine(date)
        print("{:02}/{:02}/{} est un {}".format(date[0], date[1], date[2], jour_semaine))
