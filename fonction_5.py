##Ecrire une fonction qui donne le nombre de jours depuis la précédente pleine lune pour une date
##comprise entre le 1er janvier 2000 et le 31 décembre 2010.

def jour_apres_pleine_lune(ch_date):
    nbr_jours = 0
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    li_date_1999 = [(22, 12, 1999)]
    li_dates_2000 = [(21, 1, 2000), (19, 2, 2000), (20, 3, 2000), (18, 4, 2000), (18, 5, 2000), (16, 6, 2000), (16, 7, 2000), (15, 8, 2000), (13, 9, 2000), (13, 10, 2000), (11, 11, 2000), (11, 12, 2000)]
    li_dates_2001 = [(9, 1, 2001), (8, 2, 2001), (9, 3, 2001), (8, 4, 2001), (7, 5, 2001), (6, 6, 2001), (5, 7, 2001), (4, 8, 2001), (2, 9, 2001), (2, 10, 2001), (1, 11, 2001), (30, 11, 2001), (30, 12, 2001)]
    li_dates_2002 = [(28, 1, 2002), (27, 2, 2002), (28, 3, 2002), (27, 4, 2002), (26, 5, 2002), (24, 6, 2002), (24, 7, 2002), (22, 8, 2002), (21, 9, 2002), (21, 10, 2002), (20, 11, 2002), (19, 12, 2002)]
    li_dates_2003 = [(18, 1, 2003), (16, 2, 2003), (18, 3, 2003), (16, 4, 2003), (16, 5, 2003), (14, 6, 2003), (13, 7, 2003), (13, 7, 2003), (12, 8, 2003), (10, 9, 2003), (9, 11, 2003), (8, 12, 2003)]
    li_dates_2004 = [(7, 1, 2004), (6, 2, 2004), (6, 3, 2004), (5, 4, 2004), (4, 5, 2004), (3, 6, 2004), (2, 7, 2004), (31, 7, 2004), (30, 8, 2004), (28, 9, 2004), (28, 10, 2004), (26, 11, 2004), (26, 12, 2004)]
    li_dates_2005 = [(25, 1, 2005), (24, 2, 2005), (25, 3, 2005), (24, 4, 2005), (23, 5, 2005), (22, 6, 2005), (21, 7, 2005), (19, 8, 2005), (18, 9, 2005), (17, 10, 2005), (16, 11, 2005),(15, 12, 2005)]
    li_dates_2006 = [(14, 1, 2006), (13,2, 2006), (14, 3, 2006), (13, 4, 2006), (13, 5, 2006), (11, 6, 2006), (11,7, 2006), (9, 8, 2006), (7, 9, 2006), (7, 10, 2006), (5, 11, 2006), (5, 12, 2006)]
    li_dates_2007 = [(3, 1, 2007), (2, 2, 2007), (3, 3, 2007), (2, 4, 2007), (2, 5, 2007), (1, 6, 2007), (30, 6, 2007), (30, 7, 2007), (28, 8, 2007), (26, 9, 2007), (26, 10, 2007), (24, 11, 2007), (24, 12, 2007)]
    li_dates_2008 = [(22, 1, 2008), (21, 2, 2008), (21, 3, 2008), (20, 4, 2008), (20, 5, 2008), (18, 6, 2008), (18, 7, 2008), (16, 8, 2008), (15, 9, 2008), (14, 10, 2008), (13, 11, 2008), (12, 12, 2008)]
    li_dates_2009 = [(11, 1, 2009), (9, 2, 2009), (11, 3, 2009), (9, 4, 2009), (9, 5, 2009), (7, 6, 2009), (7, 7, 2009), (6, 8, 2009), (4, 9, 2009), (4, 10, 2009), (2, 11, 2009), (2, 12, 2009)]
    li_dates_2010 = [(30, 1, 2010), (28, 2, 2010), (30, 3, 2010), (20, 4, 2010), (27, 5, 2010), (26, 6, 2010), (26, 7, 2010), (24, 8, 2010), (23, 9, 2010), (23, 10, 2010), (21, 11, 2010), (21, 12, 2010)]


    parties = ch_date.split('/') #Découpe la chaîne en trois parties : "jj", "mm", "aaaa"
    jour = int(parties[0]) #Convertit le jour en entier
    mois = int(parties[1]) #le mois
    annee = int(parties[2]) #l'année
    if annee == 2000:
        for date_lunes in li_dates_2000:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2001:
        for date_lunes in li_dates_2001:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2002:
        for date_lunes in li_dates_2002:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2003:
        for date_lunes in li_dates_2003:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2004:
        for date_lunes in li_dates_2004:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2005:
        for date_lunes in li_dates_2005:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2006:
        for date_lunes in li_dates_2006:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2007:
        for date_lunes in li_dates_2007:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2008:
        for date_lunes in li_dates_2008:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2009:
        for date_lunes in li_dates_2009:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    if annee == 2010:
        for date_lunes in li_dates_2010:
            for i in range(len(date_lunes)):
                if mois == date_lunes[1]:
                    if date_lunes[0] < jour:
                        nbr_jours = jour - date_lunes[0]
                    elif date_lunes[0] == jour:
                        nbr_jours = jours_par_mois[-1] - li_date_1999[0][0] + jour
                    else:
                        nbr_jours = 0
    return nbr_jours
