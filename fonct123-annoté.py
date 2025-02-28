# Créé par charl, le 28/02/2025 en Python 3.7

# Fonction pour vérifier si une année est bissextile
def est_bissextile(annee):
    """ Vérifie si une année est bissextile :
    - Une année est bissextile si elle est divisible par 4 et non divisible par 100,
    - Sauf si elle est aussi divisible par 400.
    """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Fonction pour lire des dates depuis un fichier texte
def lire_dates_depuis_fichier(nom_fichier):
    """ Lit un fichier contenant des dates et retourne une liste de dates.
    Chaque date doit être au format JJ/MM/AAAA. Si une ligne a un format incorrect,
    un message d'erreur est affiché.
    """
    liste_dates = []  # Liste pour stocker les dates lues

    try:
        with open(nom_fichier, 'r') as fichier:  # Ouvrir le fichier en mode lecture
            for ligne in fichier:  # Lire chaque ligne du fichier
                ligne = ligne.strip()  # Supprimer les espaces et sauts de ligne inutiles
                if ligne:  # Vérifier si la ligne n'est pas vide
                    try:
                        jour, mois, annee = map(int, ligne.split('/'))  # Convertir la ligne en trois entiers
                        liste_dates.append([jour, mois, annee])  # Ajouter la date à la liste
                    except ValueError:
                        print(f"Format incorrect dans le fichier : {ligne}")  # Afficher un message en cas d'erreur de format
    except FileNotFoundError:
        print("Fichier non trouvé. Vérifiez le chemin.")  # Gérer le cas où le fichier n'existe pas

    return liste_dates

# Fonction pour déterminer le jour de la semaine d'une date donnée
def jour_de_la_semaine(date):
    """ Calcule le jour de la semaine pour une date donnée en utilisant l'algorithme de Zeller modifié.
    Retourne le jour de la semaine sous forme de chaîne de caractères
    """
    jour, mois, annee = date

    if mois < 3:  # Janvier et février sont considérés comme les mois 13 et 14 de l'année précédente
        mois += 12
        annee -= 1

    q = jour  # Jour du mois
    m = mois  # Mois modifié
    K = annee % 100  # Deux derniers chiffres de l'année
    J = annee // 100  # Siècle de l'année

    # Formule de Zeller pour calculer le jour de la semaine
    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7

    # Liste des jours de la semaine (Zeller commence à Samedi)
    jours_semaine = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    return jours_semaine[h]

# Exécution du programme principal si ce fichier est exécuté directement
if __name__ == "__main__":
    nom_fichier = "d:/NSI/project/date.txt"  # Définition du chemin du fichier contenant les dates

    resultats = lire_dates_depuis_fichier(nom_fichier)  # Lecture des dates depuis le fichier

    for date in resultats:  # Parcourir la liste des dates lues
        jour_semaine = jour_de_la_semaine(date)  # Calcul du jour de la semaine
        print("{:02}/{:02}/{} est un {}".format(date[0], date[1], date[2], jour_semaine))  # Affichage du résultat
