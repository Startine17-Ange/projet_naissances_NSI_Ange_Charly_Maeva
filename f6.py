def lire_dates_depuis_fichier(nom_fichier):
    ''' Ouvre un fichier, extrait des dates et les renvoie sous forme de liste de dates'''
    liste_dates = []
    fichier = open(nom_fichier, 'r')

    for ligne in fichier:
        ligne = ligne.strip()
        if ligne:
            jour, mois, annee = ligne.split('/')
            # Correction pour le format d'année à 2 chiffres
            annee = 2000 + int(annee) if int(annee) < 100 else int(annee)
            # Filtrer les dates entre 2000 et 2010
            if 2000 <= annee <= 2010:
                liste_dates.append([int(jour), int(mois), annee])

    fichier.close()  # fermeture explicite du fichier
    #print("Dates extraites : ", liste_dates)
    return liste_dates


def jours_depuis_2000(date):
    '''Prend une date, calcule le nombre de jours depuis le 1er janvier 2000 et renvoie un entier'''
    jour, mois, annee = date
    compteur_jours = 0
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for annee_comp in range(2000, annee):
        if (annee_comp % 4 == 0):
            compteur_jours += 366
        else:
            compteur_jours += 365

    if (annee % 4 == 0):
        jours_par_mois[1] = 29

    for mois_comp in range(mois - 1):
        compteur_jours += jours_par_mois[mois_comp]

    compteur_jours += jour - 1

    return compteur_jours


def jour_de_la_semaine(date):
    ''' Prend une date, calcule le jour de la semaine et renvoie une chaîne de caractères'''
    jour, mois, annee = date
    compteur_jours = 0

    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    jour_reference = 5  # Samedi 1er janvier 2000, c'est un samedi donc emplacement 5 dans le tableau, jours_semaine[5]

    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (annee % 4 == 0):
        jours_par_mois[1] = 29  # Année bissextile, février a 29 jours

    for annee_comp in range(2000, annee):
        if (annee_comp % 4 == 0):
            compteur_jours += 366
        else:
            compteur_jours += 365

    for mois_comp in range(mois - 1):
        compteur_jours += jours_par_mois[mois_comp]

    compteur_jours += jour - 1

    jour_naissance = compteur_jours % 7
    jour_naissance = (jour_naissance + jour_reference) % 7
    return jours_semaine[jour_naissance]


def trouver_phase_lunaire_naissance(date_de_naissance, dates_pleines_lunes):
    jours_naissance = jours_depuis_2000(date_de_naissance)
    jours_pleines_lunes = [jours_depuis_2000(date) for date in dates_pleines_lunes]

    avant = None
    apres = None

    # Recherche de la pleine lune après la date de naissance
    for i in range(1, len(jours_pleines_lunes)):
        if jours_pleines_lunes[i] > jours_naissance:
            apres = (jours_pleines_lunes[i], dates_pleines_lunes[i])
            avant = (jours_pleines_lunes[i-1], dates_pleines_lunes[i-1])
            break
# Si aucune pleine lune après ou avant, utiliser la première ou dernière pleine lune
    apres = apres or (jours_pleines_lunes[-1], dates_pleines_lunes[-1])
    avant = avant or (jours_pleines_lunes[0], dates_pleines_lunes[0])

    return avant, apres, jours_naissance




if __name__ == "__main__":
    nom_fichier = "N:/NSI/project/date.txt"
    dates_naissance = lire_dates_depuis_fichier(nom_fichier)

    dates_pleines_lunes = [(22, 12, 1999),
                           (21, 1, 2000), (19, 2, 2000), (20, 3, 2000), (18, 4, 2000), (18, 5, 2000), (16, 6, 2000), (16, 7, 2000), (15, 8, 2000), (13, 9, 2000), (13, 10, 2000), (11, 11, 2000), (11, 12, 2000),
                           (9, 1, 2001), (8, 2, 2001), (9, 3, 2001), (8, 4, 2001), (7, 5, 2001), (6, 6, 2001), (5, 7, 2001), (4, 8, 2001), (2, 9, 2001), (2, 10, 2001), (1, 11, 2001), (30, 11, 2001), (30, 12, 2001),
                           (28, 1, 2002), (27, 2, 2002), (28, 3, 2002), (27, 4, 2002), (26, 5, 2002), (24, 6, 2002), (24, 7, 2002), (22, 8, 2002), (21, 9, 2002), (21, 10, 2002), (20, 11, 2002), (19, 12, 2002),
                           (18, 1, 2003), (16, 2, 2003), (18, 3, 2003), (16, 4, 2003), (16, 5, 2003), (14, 6, 2003), (13, 7, 2003), (13, 7, 2003), (12, 8, 2003), (10, 9, 2003),(10,10,2003), (9, 11, 2003), (8, 12, 2003),
                           (7, 1, 2004), (6, 2, 2004), (6, 3, 2004), (5, 4, 2004), (4, 5, 2004), (3, 6, 2004), (2, 7, 2004), (31, 7, 2004), (30, 8, 2004), (28, 9, 2004), (28, 10, 2004), (26, 11, 2004), (26, 12, 2004),
                           (25, 1, 2005), (24, 2, 2005), (25, 3, 2005), (24, 4, 2005), (23, 5, 2005), (22, 6, 2005), (21, 7, 2005), (19, 8, 2005), (18, 9, 2005), (17, 10, 2005), (16, 11, 2005),(15, 12, 2005),
                           (14, 1, 2006), (13,2, 2006), (14, 3, 2006), (13, 4, 2006), (13, 5, 2006), (11, 6, 2006), (11,7, 2006), (9, 8, 2006), (7, 9, 2006), (7, 10, 2006), (5, 11, 2006), (5, 12, 2006),
                           (3, 1, 2007), (2, 2, 2007), (3, 3, 2007), (2, 4, 2007), (2, 5, 2007), (1, 6, 2007), (30, 6, 2007), (30, 7, 2007), (28, 8, 2007), (26, 9, 2007), (26, 10, 2007), (24, 11, 2007), (24, 12, 2007),
                           (22, 1, 2008), (21, 2, 2008), (21, 3, 2008), (20, 4, 2008), (20, 5, 2008), (18, 6, 2008), (18, 7, 2008), (16, 8, 2008), (15, 9, 2008), (14, 10, 2008), (13, 11, 2008), (12, 12, 2008),
                           (11, 1, 2009), (9, 2, 2009), (11, 3, 2009), (9, 4, 2009), (9, 5, 2009), (7, 6, 2009), (7, 7, 2009), (6, 8, 2009), (4, 9, 2009), (4, 10, 2009), (2, 11, 2009), (2, 12, 2009),(31,12,2009),
                           (30, 1, 2010), (28, 2, 2010), (30, 3, 2010), (28, 4, 2010), (27, 5, 2010), (26, 6, 2010), (26, 7, 2010), (24, 8, 2010), (23, 9, 2010), (23, 10, 2010), (21, 11, 2010), (21, 12, 2010),
                           (19, 1, 2011)]


for date_naissance in dates_naissance:
    # Récupère les informations sur la phase lunaire
    avant, apres, jours_naissance = trouver_phase_lunaire_naissance(date_naissance, dates_pleines_lunes)

    # Affiche la date de naissance
    print("Date de naissance: %s %d/%d/%d" % (jour_de_la_semaine(date_naissance),date_naissance[0],date_naissance[1],date_naissance[2]))

    # Affiche la dernière pleine lune avant la naissance, si elle existe
    if avant:
        print("Dernière pleine lune avant naissance: %d/%d/%d (%d jours avant)" % (avant[1][0],avant[1][1],avant[1][2],jours_naissance - avant[0]))
    # Affiche la première pleine lune après la naissance, si elle existe
    if apres:
        print("Première pleine lune après naissance: %d/%d/%d (%d jours après)" % (apres[1][0],apres[1][1],apres[1][2],apres[0] - jours_naissance))
    # Ligne vide pour séparer les résultats
    print("")
