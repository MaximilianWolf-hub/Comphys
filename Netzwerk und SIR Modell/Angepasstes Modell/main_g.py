from SIR_g import infectODEsolverAll, sus, inf, rec, vac, des, exp
from Reisebewegungen import travel
from Europakarte_g import create_map
import numpy as np

second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON') #Start der Epedemie in London
inf[index, 0] = 1000 #Anfängliche Zhal der infizierten

sus_list = sus[:, 0].tolist()
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()
vac_list = vac[:, 0].tolist()
des_list = des[:, 0].tolist()
exp_list = exp[:, 0].tolist()

pt = 0.01       #hier legen wir die Reisewahrscheinlich 1% fest

#
all_suspects = np.array([sus_list])             #diese Listen speichern gleich in jeder Spalte die aktuellen S-Populationen, Infektionszahlen und Genesenen, Geimpfte, Exponierte und Verstorbene
all_infections = np.array([inf_list])           #aus jeder Stadt in der selben Reihenfolge wie in cities
all_recovered = np.array([rec_list])            #also jede Zeile wird die Entwicklung der Populationen einer Stadt über einen bestimmten Zeitraum angeben
all_vaccinated = np.array([vac_list])
all_deceased = np.array([des_list])
all_exposed = np.array([exp_list])

# Simulation über 365 Tage
for i in range(60):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list, sus_list, inf_list, rec_list, pt)   #hier simulieren wir erst die Reisebewegungen der Populationen mit
    inf_list = travel(inf_list, sus_list, inf_list, rec_list, pt)   #der Funktion travel aus dem Modul Reisebewegungen
    rec_list = travel(rec_list, sus_list, inf_list, rec_list, pt)
    vac_list = travel(vac_list, sus_list, inf_list, rec_list, pt)
    des_list = travel(des_list, sus_list, inf_list, rec_list, pt)
    exp_list = travel(exp_list, sus_list, inf_list, rec_list, pt)

    all_suspects = np.vstack((all_suspects, sus_list))              #die aktuellen Populationen werden den Listen für die Entwicklung der Populationen
    all_infections = np.vstack((all_infections, inf_list))          #hinzugefügt
    all_recovered = np.vstack((all_recovered, rec_list))
    all_vaccinated = np.vstack((all_vaccinated, vac_list))
    all_exposed = np.vstack((all_exposed, exp_list))
    all_deceased = np.vstack((all_deceased, des_list))

    # Simuliere Infektionen mit Euler-Verfahren
    infectODEsolverAll(sus_list, inf_list, rec_list, vac_list, des_list, exp_list)    #wir lösen die DGL in allen Städten mit der gewünschten Methode
    #infectRK4All(sus_list, inf_list, rec_list, exp_list, vac_list, des_list)
    #infectEulerAll(sus_list, inf_list, rec_list, exp_list, vac_list, des_list)
    print('Tag:', i+1)

#Erstelle Karte mit Daten nach geüwnschtem Zeitraum
create_map(all_suspects, all_infections, all_recovered, all_vaccinated, all_deceased, all_exposed)
