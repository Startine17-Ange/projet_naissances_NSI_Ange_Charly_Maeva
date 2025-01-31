﻿##Ecrire une fonction qui donne le nombre de jours depuis la précédente pleine lune pour une date
##comprise entre le 1er janvier 2000 et le 31 décembre 2010.

def jour_apres_pleine_lune(date):
    nbr_jours = 0
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    li_dates_2000 = [('21', '01', '2000'), ('19', '02', '2000'),('20', '03', '2000'), ('18', '04', '2000'), ('18', '05', '2000'), ('16', '06', '2000'), ('16', '07', '2000'), ('15', '08', '2000'), ('13', '09', '2000'), ('13', '10', '2000'), ('11', '11', '2000'), ('11', '12', '2000')]
    li_dates_2001 = [('09', '01', '2001'), ('08', '02', '2001'), ('09', '03', '2001'), ('08', '04', '2001'), ('07', '05', '2001'), ('06', '06', '2001'), ('05', '07', '2001'), ('04', '08', '2001'), ('02', '09', '2001'), ('02', '10', '2001'), ('01', '11', '2001'), ('30', '11', '2001'), ('30', '12', '2001')]
    li_dates_2002 = [('28', '01', '2002'), ('27', '02', '2002'), ('28', '03', '2002'), ('27', '04', '2002'), ('26', '05', '2002'), ('24', '06', '2002'), ('24', '07', '2002'), ('22', '08', '2002'), ('21', '09', '2002'), ('21', '10', '2002'), ('20', '11', '2002'), ('19', '12', '2002')]
    li_dates_2003 = [('18', '01', '2003'), ('16', '02', '2003'), ('18', '03', '2003'), ('16', '04', '2003'), ('16', '05', '2003'), ('14', '06', '2003'), ('13/07/2003'), ('13/07/2003'), ('12', '08', '2003'), ('10', '09', '2003'), ('09', '11', '2003'), ('08', '12', '2003')]
    li_dates_2004 = [('07', '01', '2004'), ('06', '02', '2004'), ('06', '03', '2004'), ('05', '04', '2004'), ('04', '05', '2004'), ('03', '06', '2004'), ('02', '07', '2004'), ('31', '07', '2004'), ('30', '08', '2004'), ('28', '09', '2004'), ('28', '10', '2004'), ('26', '11', '2004'), ('26', '12', '2004')]
    li_dates_2005 = [('25', '01', '2005'), ('24', '02', '2005'), ('25', '03', '2005'), ('24', '04', '2005'), ('23', '05', '2005'), ('22', '06', '2005'), ('21', '07', '2005'), ('19', '08', '2005'), ('18', '09', '2005'), ('17', '10', '2005'), ('16', '11', '2005'), ('15', '12', '2005')]
    li_dates_2006 = [('14', '01', '2006'), ('13', '02', '2006'), ('14', '03', '2006'), ('13', '04', '2006'), ('13', '05', '2006'), ('11', '06', '2006'), ('11', '07', '2006'), ('09', '08', '2006'), ('07', '09', '2006'), ('07', '10', '2006'), ('05', '11', '2006'), ('05', '12', '2006')]
    li_dates_2007 = [('03', '01', '2007'), ('02', '02', '2007'), ('03', '03', '2007'), ('02', '04', '2007'), ('02', '05', '2007'), ('01', '06', '2007'), ('30', '06', '2007'), ('30', '07', '2007'), ('28', '08', '2007'), ('26', '09', '2007'), ('26', '10', '2007'), ('24', '11', '2007'), ('24', '12', '2007')]
    li_dates_2008 = [('22', '01', '2008'), ('21', '02', '2008'), ('21', '03', '2008'), ('20', '04', '2008'),('20', '05', '2008'), ('18', '06', '2008'), ('18', '07', '2008'), ('16', '08', '2008'), ('15', '09', '2008'), ('14', '10', '2008'), ('13', '11', '2008'), ('12', '12', '2008')]
    li_dates_2009 = [('11', '01', '2009'), ('09', '02', '2009'), ('11', '03', '2009'), ('09', '04', '2009'),('09', '05', '2009'), ('07', '06', '2009'), ('07', '07', '2009'), ('06', '08', '2009'), ('04', '09', '2009'), ('04', '10', '2009'), ('02', '11', '2009'), ('02', '12', '2009')]
    li_dates_2010 = [('30', '01', '2010') ('28', '02', '2010'), ('30', '03', '2010'), ('20', '04', '2010'), ('27', '05', '2010'), ('26', '06', '2010'), ('26', '07', '2010'), ('24', '08', '2010'), ('23', '09', '2010'), ('23', '10', '2010'), ('21', '11', '2010'), ('21', '12', '2010')]
    for date in li_dates:
        parties = date.split('/') #Découpe la chaîne en trois parties : "jj", "mm", "aaaa"
        jour = int(parties[0]) #Convertit le jour en entier
        mois = int(parties[1]) #le mois
        annee = int(parties[2]) #l'année
        if annee == '2000':
            for ch_date_lunes in li_dates_2000:
                for i in range(len(ch_date_lunes)):
                    if mois == ch_date_lunes[1]:
                        if ch_date_lunes[0] < jour:
                            nbr_jours = jour - ch_date_lunes[0]
                        else:
                            ch_date_lunes[i-1]
                            nbr_jours = jours_par_mois[i] - ch_date_lunes[0] + jour
    return nbr_jours