from SIRFunktionenEuAf import infectODEsolverAllEuAf, sus, inf, rec
from ReisefunktionenVerbindung import travelCombined
import numpy as np
from KarteVerbindung import create_map

second_column_list = sus[:, 1].tolist()       # Wir wollen den Index der Stadt herausfinden, bei der eine
index = second_column_list.index('LONDON')    #Epidemie wird in dieser Stadt gestartet wird
inf[index, 0] = 1000                          #und wir setzen die Anzahl an Infizierten auf 1000

sus_list = sus[:, 0].tolist()       #sus_list, inf_list und rec_list enthalten jeweils die aktuellen Zahlen von
inf_list = inf[:, 0].tolist()       #S-Population, Infizierten und Genesenen
rec_list = rec[:, 0].tolist()

pt = 0.01                        #Hier legen wir die Reisewahrscheinlichkeit auf 1% fest

all_suspects = np.array([sus_list])    #Diese Listen speichern in jeder Spalte die aktuellen S-Populationen, Infektionszahlen und Genesenen
all_infections = np.array([inf_list])  #aus jeder Stadt.
all_recovered = np.array([rec_list])   #Also jede Zeile wird die Entwicklung der Populationen einer Stadt über einen bestimmten Zeitraum angeben

time_span = 600    #Zeitspanne, über die die Krankheit sich ausbreitet

for i in range(time_span): #Schleife über Zeitspanne
    sus_list = travelCombined(sus_list, pt)         # Hier simulieren wir erst die Reisebewegungen der Populationen mit
    inf_list = travelCombined(inf_list, pt)         # der Funktion travelCombined aus Reisefunktionenverbindung
    rec_list = travelCombined(rec_list, pt)

    all_suspects = np.vstack((all_suspects, sus_list))          #Die aktuellen Populationen werden den Listen
    all_infections = np.vstack((all_infections, inf_list))      #für die Entwicklung der Populationen hinzugefügt
    all_recovered = np.vstack((all_recovered, rec_list))

    infectODEsolverAllEuAf(sus_list, inf_list, rec_list)   #Simuliere Infektionen mit der gewünschten Methode
    #Wir lösen die DGL in allen Städten mit der gewünschten Methode
    #infectRK4All(sus_list, inf_list, rec_list)
    #infectEulerAll(sus_list, inf_list, rec_list)
    print('Tag:', i+1)  #i+1 damit der aktuelle Tag mit berücksichtigt wird

#Erstellt eine Karte mit Daten nach gewünschtem Zeitraum mit den Verläufen der Populationszahlen
create_map(all_suspects, all_infections, all_recovered)
