#ch_fichier = open('PN_test.csv', 'r')
def fonction_jour_dimanche(ch_fichier):
    li_infos = []
    li_dates = []
    li_sexes = []
    for info in ch_fichier:
        li_infos.append(info.split(";"))
    for li_date_sexe in li_infos :
        for i in range(len(li_date_sexe)):
            if i % 2 == 0:
                li_dates.append(li_date_sexe[i])
##                li_dates.remove('Né(e) le')
        else :
            li_sexes.append(li_date_sexe[i])
##            li_sexes.remove('Sexe\n')
    for element in li_(dates):
        # Liste des jours de la semaine
        jours_semaines = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

        # Nombre de jours par mois (pour une année non bissextile)
        jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # On découpe la chaîne( en format "jj/mm/aaaa")
        # Chaque partie (jour, mois, année) est convertie en nombre entier
        for date in li_dates:
            parties = date.split('/') # Découpe la chaîne en trois parties : "jj", "mm", "aaaa"
            jour = int(parties[0]) # Convertit le jour en entier
            mois = int(parties[1]) #    //      le mois   //
            annee = int(parties[2]) #    //     l'année    //

        # Vérifie si l'année est bissextile
        bissextile = annee % 4 == 0

        # Vérifie le nombre de jours dans le mois
        jours_max = jours_par_mois[mois - 1]
        if mois == 2 and bissextile:
            jours_max = 29
        if jour > jours_max:
            print( "Le mois {mois} de l'année {annee} n'a que {jours_max} jours.")

    # Calcul du nombre total de jours écoulés depuis le 1er janvier 2000
        jours_totaux = 0

        # Ajouter les jours des années complètes entre 2000 et l'année précédente
        for i in range(2000, annee):
             if i % 4 == 0 :
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

        jour=jours_semaines[index_jour]

        liste_valeur=[0,0,0,0,0,0,0]
        if jour =='lundi':
            liste_valeur[0]=liste_valeur[0]+1
        elif jour =='mardi':
            liste_valeur[1]=liste_valeur[1]+1
        elif jour =='mercredi':
            liste_valeur[2]=liste_valeur[2]+1
        elif jour =='jeudi':
            liste_valeur[3]=liste_valeur[3]+1
        elif jour =='vendredi':
            liste_valeur[4]=liste_valeur[4]+1
        elif jour =='samedi':
            liste_valeur[5]=liste_valeur[5]+1
        elif jour =='dimanche':
            liste_valeur[6]=liste_valeur[6]+1
    return liste_valeur
