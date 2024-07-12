from SIR_Funktionen import infectODEsolverAll, infectRK4All, infectEulerAll, sus, inf, rec
from Reisebewegungen import travel
import numpy as np
from New_Europakerte import create_map

second_column_list = sus[:, 1].tolist()             #Wir wollen den Index der Stadt London herausfinden, bei der eine
index = second_column_list.index('LONDON')          #Epidemie gestartet wird und setzten die Anzahl an infizierten auf 1000
inf[index, 0] = 1000


sus_list = sus[:, 0].tolist()       #sus_list, inf_list und rec_list enthalten jeweils die aktuellen Zahlen von
inf_list = inf[:, 0].tolist()       # S-Population, Infizierten und Genesenen
rec_list = rec[:, 0].tolist()

pt = 0.01                           #hier legen wir die Reisewahrscheinlich 1% fest


all_suspects = np.array([sus_list])         #diese Listen speichern gleich in jeder Spalte die aktuellen S-Populationen, Infektionszahlen und Genesenen
all_infections = np.array([inf_list])       #aus jeder Stadt in der selben Reihenfolge wie in cities
all_recovered = np.array([rec_list])        #also jede Zeile wird die Entwicklung der Populationen einer Stadt über einen bestimmten Zeitraum angeben

time_span = 800     #die Zeitspanne, über die die Krankheit sich ausbreitet


# Simulation über 365 Tage
for i in range(time_span):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list, pt)         #hier simulieren wir erst die Reisebewegungen der Populationen mit
    inf_list = travel(inf_list, pt)         #der Funktion travel aus dem Modul Reisebewegungen
    rec_list = travel(rec_list, pt)

    all_suspects = np.vstack((all_suspects, sus_list))          #die aktuellen Populationen werden den Listen für die Entwicklung der Populationen
    all_infections = np.vstack((all_infections, inf_list))      #hinzugefügt
    all_recovered = np.vstack((all_recovered, rec_list))

    # Simuliere Infektionen mit Euler-Verfahren
    infectODEsolverAll(sus_list, inf_list, rec_list)            #wir lösen die DGL in allen Städten mit der gewünschten Methode
    #infectRK4All(sus_list, inf_list, rec_list)
    #infectEulerAll(sus_list, inf_list, rec_list)
    print('Tag:', i)



#Erstelle Karte mit Daten nach geüwnschtem Zeitraum mit den Verläufen der Populationszahlen
create_map(all_suspects, all_infections, all_recovered)

