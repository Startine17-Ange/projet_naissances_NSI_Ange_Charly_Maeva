## a entrer dans la console dico_fichier = open('PN_test.csv', 'r') :

def extraire_fichier(dico_fichier):
    li_dates = []
    for date, sexe in dico_fichier.items():
        li_dates.append(date)
    return li_dates
