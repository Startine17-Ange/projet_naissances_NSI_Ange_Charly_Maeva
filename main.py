## a entrer dans la console ch_fichier = open('PN_test.csv', 'r')

def extraire_fichier(ch_fichier):
    li_info = []
    li_dates = []
    li_sexes = []
    for info in ch_fichier:
        li_info.append(info)
        li_info.split(";")
    for i in range(len(li_info)):
        if i % 2 == 1:
            li_dates.append(li_info[i])
        else :
            li_sexes.append(li_info[i])
    return li_dates

##et ne pas oublier ch_fichier.close()