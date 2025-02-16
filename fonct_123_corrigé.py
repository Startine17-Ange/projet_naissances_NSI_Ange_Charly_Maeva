# Créé par charl, le 15/02/2025 en Python 3.7
def read_dates_from_file(filename):
    dates_list = []
    with open(filename, 'r') as file:#lire le fichier .txt
        for line in file:
            line = line.strip() #lie la ligne du dossier .txt et le stock
            if line:
                day, month, year = line.split(';')#on separe les variable avant et apres les ; dans 3 variable connue sou forme de tableau [jour,mois,année]
                dates_list.append([int(day), int(month), int(year)])#on ajoute ces donnes dans un tableau qui liqte les dates
    return dates_list

def day_of_week(date):
    day, month, year = date #On récupére le tableau des date sous la forme [jour,mois,année] et on les place dans 3 variables
    days_count = 0 #on initialisa le nombre de jour qui sépare 1 janvier 2000 à la date de naissance

    jour_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi','Dimanche']
    reference_day = 5  # Samedi 1er janvier 2000, c'est un samedi donc emplacement 5 dans le tableau, jour_semaine[5]

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0): #on verifie que l'année est bien un multiple de 4, avec b=year%4=0 pour l'equation years = a.4+b
        days_in_month[1] = 29  # Année bissextile alors fevriere à 29 jours

    for y in range(2000, year): #on conte le nombre de jour entre 2000 et l annee de naisssance
        if (y % 4 == 0):
            days_count += 366
        else:
            days_count += 365
    for m in range(month - 1):#On ajoute à days_count le nombre de mois entre janvier (mois 1 et 0 dans le tableau) et le moi de naissance
        days_count += days_in_month[m] #somme des mois depuis janvier dans le tablea days_in_mouths

    days_count += day - 1 #on ajoute le nombre de jour en le 1er du mois et le jour de naissance

    jour_naissance = days_count % 7 #il y a 7 jour dans une semaine, on regarde b=jour_naissance dans la fonction days_count=a.7+b
    jour_naissance = (jour_naissance+reference_day)%7 #car le 1er janvier est un samedie et non un lundi, %7 car on est toujours sur 7 jour dans la semaines
    return jour_semaine[jour_naissance]

if __name__ == "__main__":
    filename = "D:/NSI/project/date.txt"  # Remplace par ton fichier
    result = read_dates_from_file(filename)  # Ajout de l'appel à read_dates_from_file

    for date in result:
        weekday = day_of_week(date)
        print(f"{date[0]:02}/{date[1]:02}/{date[2]} est un {weekday}")
