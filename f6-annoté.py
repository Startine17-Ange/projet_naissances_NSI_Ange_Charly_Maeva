# Créé par charl, le 28/02/2025 en Python 3.7

def lire_dates_depuis_fichier(nom_fichier):
    """
    Lit un fichier contenant des dates et filtre celles entre 2000 et 2010.
    :param nom_fichier: Nom du fichier contenant les dates (format jj/mm/aa)
    :return: Liste des dates valides sous forme de listes [jour, mois, année]
    """
    liste_dates = []
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne:
                jour, mois, annee = ligne.split('/')
                annee = 2000 + int(annee) if int(annee) < 100 else int(annee)
                if 2000 <= annee <= 2010:
                    liste_dates.append([int(jour), int(mois), annee])
    print("Dates extraites : ", liste_dates)
    return liste_dates

def jours_depuis_2000(date):
    """
    Calcule le nombre de jours écoulés depuis le 1er janvier 2000.
    :param date: Liste [jour, mois, année]
    :return: Nombre de jours écoulés
    """
    jour, mois, annee = date
    compteur_jours = 0
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajouter les jours des années complètes
    for annee_comp in range(2000, annee):
        compteur_jours += 366 if (annee_comp % 4 == 0) else 365

    # Ajustement pour année bissextile
    if annee % 4 == 0:
        jours_par_mois[1] = 29

    # Ajouter les jours des mois complets
    for mois_comp in range(mois - 1):
        compteur_jours += jours_par_mois[mois_comp]

    # Ajouter les jours du mois actuel
    compteur_jours += jour - 1
    return compteur_jours

def jour_de_la_semaine(date):
    """
    Détermine le jour de la semaine pour une date donnée.
    :param date: Liste [jour, mois, année]
    :return: Nom du jour de la semaine
    """
    jour, mois, annee = date
    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    jour_reference = 5  # 1er janvier 2000 était un samedi
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if annee % 4 == 0:
        jours_par_mois[1] = 29

    compteur_jours = jours_depuis_2000(date)
    jour_naissance = (compteur_jours + jour_reference) % 7
    return jours_semaine[jour_naissance]

def trouver_phase_lunaire_naissance(date_de_naissance, dates_pleines_lunes):
    """
    Trouve la pleine lune la plus proche de la date de naissance.
    :param date_de_naissance: Liste [jour, mois, année]
    :param dates_pleines_lunes: Liste des dates de pleines lunes
    :return: Dernière et prochaine pleine lune ainsi que les jours écoulés depuis 2000
    """
    jours_naissance = jours_depuis_2000(date_de_naissance)
    jours_pleines_lunes = [jours_depuis_2000(date) for date in dates_pleines_lunes]

    avant, apres = None, None

    for i in range(1, len(jours_pleines_lunes)):
        if jours_pleines_lunes[i] > jours_naissance:
            apres = (jours_pleines_lunes[i], dates_pleines_lunes[i])
            avant = (jours_pleines_lunes[i-1], dates_pleines_lunes[i-1])
            break

    if apres is None and jours_pleines_lunes:
        apres = (jours_pleines_lunes[-1], dates_pleines_lunes[-1])
    if avant is None and jours_pleines_lunes:
        avant = (jours_pleines_lunes[0], dates_pleines_lunes[0])

    return avant, apres, jours_naissance

if __name__ == "__main__":
    """
    Programme principal qui lit les dates de naissance, détermine leur jour de la semaine et leur phase lunaire.
    """
    nom_fichier = "d:/NSI/project/date.txt"
    dates_naissance = lire_dates_depuis_fichier(nom_fichier)

    dates_pleines_lunes = [(22, 12, 1999), (21, 1, 2000), (19, 2, 2000), (20, 3, 2000), (18, 4, 2000)]  # Extrait

    for date_naissance in dates_naissance:
        avant, apres, jours_naissance = trouver_phase_lunaire_naissance(date_naissance, dates_pleines_lunes)
        print("Date de naissance: {} {}/{}/{}".format(jour_de_la_semaine(date_naissance), str(date_naissance[0]).zfill(2), str(date_naissance[1]).zfill(2), date_naissance[2]))
        if avant:
            print("Dernière pleine lune avant naissance: {}/{}/{} ({} jours avant)".format(str(avant[1][0]).zfill(2), str(avant[1][1]).zfill(2), avant[1][2], jours_naissance - avant[0]))
        if apres:
            print("Première pleine lune après naissance: {}/{}/{} ({} jours après)".format(str(apres[1][0]).zfill(2), str(apres[1][1]).zfill(2), apres[1][2], apres[0] - jours_naissance))
        print()

