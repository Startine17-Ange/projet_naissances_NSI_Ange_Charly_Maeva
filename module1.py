
# Fonction principale
def fonct_J(li_dates):
    # Liste des jours de la semaine
    jours_semaines = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

    # Nombre de jours par mois (pour une année non bissextile)
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        # On découpe la chaîne( en format "jj/mm/aaaa")
        # Chaque partie (jour, mois, année) est convertie en nombre entier
        for date in li_dates:
            parties = date.split('/') # Découpe la chaîne en trois parties : "jj", "mm", "aaaa"
            jour = int(parties[0]) # Convertit le jour en entier
            mois = int(parties[1]) #    //      le mois   //
            annee = int(parties[2]) #    //     l'année    //
        except ValueError: # empeche valeur pas = nombre
        return "c'est écrit dans un format incorrect. Entrez la date sous la forme jj/mm/aaaa."

    # Vérifications de base
    if annee < 2000 or annee > 2010:
        return "L'année doit être comprise entre 2000 et 2010."
    if mois < 1 or mois > 12:
        return "Le mois doit être entre 1 et 12."
    if jour < 1 or jour > 31:
        return "Le jour doit être entre 1 et 31."

    # Vérifie si l'année est bissextile
    bissextile = annee % 4 == 0 and  annee % 400 == 0

    # Vérifie le nombre de jours dans le mois
    jours_max = jours_par_mois[mois - 1]
    if mois == 2 and bissextile:
        jours_max = 29
    if jour > jours_max:
        return "Le mois {mois} de l'année {annee} n'a que {jours_max} jours."

    # Calcul du nombre total de jours écoulés depuis le 1er janvier 2000
    jours_totaux = 0

    # Ajouter les jours des années complètes entre 2000 et l'année précédente
    for i in range(2000, annee):
         if i % 4 == 0 and  i % 400 == 0:
            jours_totaux = 366
         else:
            jours_totaux= 365

    # Ajouter les jours des mois complets de l'année donnée
    for m in range(mois - 1):
        jours_totaux += jours_par_mois[m]
        # Ajouter 1 jour pour février si l'année est bissextile
        if m == 1 and bissextile:
            jours_totaux += 1

    # Ajouter les jours du mois en cours
    jours_totaux += jour - 1

    # Trouver le jour de la semaine correspondant
    index_jour = (jours_totaux + 6) % 7 # +6 car 1er janvier 2000 était un samedi
    return jours_semaines[index_jour]

# Exemple d'utilisation
date = input("Entrez une date au format jj/mm/aaaa : ")
print(jour_semaine_depuis_2000_chaine(date))
