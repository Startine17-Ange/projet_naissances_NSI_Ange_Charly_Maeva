﻿## a entrer dans la console ch_fichier = open('PN_test.csv', 'r')

def extraire_fichier(ch_fichier):
    li_infos = []
    li_dates = []
    li_sexes = []
    dico_dates_sexes = {}
    for info in ch_fichier:
        li_infos.append(info.split(";"))
    for li_date_sexe in li_infos :
        for i in range(len(li_date_sexe)):
            if i % 2 == 0:
                if dico_dates_sexes[date] in li_infos:
                    dico_dates_sexes[date] += sexe
                li_dates.append(li_date_sexe[i])
##                li_dates.remove('Né(e) le')
        else :
            li_sexes.append(li_date_sexe[i])
            dico_dates_sexes[date] += sexe
##            li_sexes.remove('Sexe\n')
    return li_dates, li_sexes, dico_dates_sexes

##et ne pas oublier ch_fichier.close()
