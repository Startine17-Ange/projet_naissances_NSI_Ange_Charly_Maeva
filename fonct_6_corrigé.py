# Créé par charl, le 15/02/2025 en Python 3.7
def read_dates_from_file(filename):
    dates_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                day, month, year = line.split(';')
                dates_list.append([int(day), int(month), int(year)])
    return dates_list


def days_since_2000(date):
    day, month, year = date
    days_count = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for y in range(2000, year):
        if (y % 4 == 0):
            days_count += 366
        else:
            days_count += 365

    if (year % 4 == 0):
        days_in_month[1] = 29

    for m in range(month - 1):
        days_count += days_in_month[m]

    days_count += day - 1

    return days_count

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

def find_moon_phase_birth(date_of_birth, full_moon_dates):
    birth_days = days_since_2000(date_of_birth)
    days_full_moons = [days_since_2000(date) for date in full_moon_dates]

    # Correction: forcer la première date de pleine lune à -9 jours du 01/01/2000

    for i in range(1, len(days_full_moons)):
        if days_full_moons[i] > birth_days:
            after = (days_full_moons[i], full_moon_dates[i])
            before = (days_full_moons[i-1], full_moon_dates[i-1])
            break

    if before is None:
        before = (days_full_moons[-1], full_moon_dates[-1])

    return before, after, birth_days

if __name__ == "__main__":
    filename = "D:/NSI/project/date.txt"
    birth_dates = read_dates_from_file(filename)

    full_moon_dates = [(22, 12, 1999),
                       (21, 1, 2000), (19, 2, 2000), (20, 3, 2000), (18, 4, 2000), (18, 5, 2000), (16, 6, 2000), (16, 7, 2000), (15, 8, 2000), (13, 9, 2000), (13, 10, 2000), (11, 11, 2000), (11, 12, 2000),
                       (9, 1, 2001), (8, 2, 2001), (9, 3, 2001), (8, 4, 2001), (7, 5, 2001), (6, 6, 2001), (5, 7, 2001), (4, 8, 2001), (2, 9, 2001), (2, 10, 2001), (1, 11, 2001), (30, 11, 2001), (30, 12, 2001),
                       (28, 1, 2002), (27, 2, 2002), (28, 3, 2002), (27, 4, 2002), (26, 5, 2002), (24, 6, 2002), (24, 7, 2002), (22, 8, 2002), (21, 9, 2002), (21, 10, 2002), (20, 11, 2002), (19, 12, 2002),
                       (18, 1, 2003), (16, 2, 2003), (18, 3, 2003), (16, 4, 2003), (16, 5, 2003), (14, 6, 2003), (13, 7, 2003), (13, 7, 2003), (12, 8, 2003), (10, 9, 2003), (9, 11, 2003), (8, 12, 2003),
                       (7, 1, 2004), (6, 2, 2004), (6, 3, 2004), (5, 4, 2004), (4, 5, 2004), (3, 6, 2004), (2, 7, 2004), (31, 7, 2004), (30, 8, 2004), (28, 9, 2004), (28, 10, 2004), (26, 11, 2004), (26, 12, 2004),
                       (25, 1, 2005), (24, 2, 2005), (25, 3, 2005), (24, 4, 2005), (23, 5, 2005), (22, 6, 2005), (21, 7, 2005), (19, 8, 2005), (18, 9, 2005), (17, 10, 2005), (16, 11, 2005),(15, 12, 2005),
                       (14, 1, 2006), (13,2, 2006), (14, 3, 2006), (13, 4, 2006), (13, 5, 2006), (11, 6, 2006), (11,7, 2006), (9, 8, 2006), (7, 9, 2006), (7, 10, 2006), (5, 11, 2006), (5, 12, 2006),
                       (3, 1, 2007), (2, 2, 2007), (3, 3, 2007), (2, 4, 2007), (2, 5, 2007), (1, 6, 2007), (30, 6, 2007), (30, 7, 2007), (28, 8, 2007), (26, 9, 2007), (26, 10, 2007), (24, 11, 2007), (24, 12, 2007),
                       (22, 1, 2008), (21, 2, 2008), (21, 3, 2008), (20, 4, 2008), (20, 5, 2008), (18, 6, 2008), (18, 7, 2008), (16, 8, 2008), (15, 9, 2008), (14, 10, 2008), (13, 11, 2008), (12, 12, 2008),
                       (11, 1, 2009), (9, 2, 2009), (11, 3, 2009), (9, 4, 2009), (9, 5, 2009), (7, 6, 2009), (7, 7, 2009), (6, 8, 2009), (4, 9, 2009), (4, 10, 2009), (2, 11, 2009), (2, 12, 2009),
                       (30, 1, 2010), (28, 2, 2010), (30, 3, 2010), (20, 4, 2010), (27, 5, 2010), (26, 6, 2010), (26, 7, 2010), (24, 8, 2010), (23, 9, 2010), (23, 10, 2010), (21, 11, 2010), (21, 12, 2010),
                       (19, 1, 2011)]

    for birth_date in birth_dates:
        before, after, birth_days = find_moon_phase_birth(birth_date, full_moon_dates)
        print(f"Date de naissance: {day_of_week(birth_date)} {birth_date[0]}/{birth_date[1]}/{birth_date[2]}")
        if before:
            print(f"Dernière pleine lune avant naissance: {before[1][0]}/{before[1][1]}/{before[1][2]} ({birth_days - before[0]} jours avant)")
        if after:
            print(f"Première pleine lune après naissance: {after[1][0]}/{after[1][1]}/{after[1][2]} ({after[0] - birth_days} jours après)")
        print()
