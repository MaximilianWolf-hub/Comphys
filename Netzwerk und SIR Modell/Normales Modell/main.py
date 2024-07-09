from SIR_Funktionen import infectODEsolverAll, sus, inf, rec
from Reisebewegungen import travel
import matplotlib.pyplot as plt
import numpy as np
from New_Europakerte import create_map

second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON')
inf[index, 0] = 1000


sus_list = sus[:, 0].tolist()
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()

pt = 0.01

sus_London = []
inf_London = []
rec_London = []


all_suspects = np.array([sus_list])
all_infections = np.array([inf_list])
all_recovered = np.array([rec_list])

# Simulation über 365 Tage
for i in range(365):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list, pt)
    inf_list = travel(inf_list, pt)
    rec_list = travel(rec_list, pt)

    all_suspects = np.vstack((all_suspects, sus_list))
    all_infections = np.vstack((all_infections, inf_list))
    all_recovered = np.vstack((all_recovered, rec_list))

    # Simuliere Infektionen mit Euler-Verfahren
    infectODEsolverAll(sus_list, inf_list, rec_list)
    print('Tag:', i)



for i in range(len(sus_list)):
    sus[i, 0] = sus_list[i]
    inf[i, 0] = inf_list[i]
    rec[i, 0] = rec_list[i]


#Erstelle Karte mit Daten nach geüwnschtem Zeitraum
create_map(all_suspects, all_infections, all_recovered)

