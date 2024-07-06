from SIR_Funktionen import infectEulerAll, infectRK4All, infectODEsolverAll, sus, inf, rec
from Reisebewegungen import travel
from Europakarte import create_map

second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON')
inf[index, 0] = 1000


sus_list = sus[:, 0].tolist()
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()





# Simulation über 365 Tage
for i in range(365):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list)
    inf_list = travel(inf_list)
    rec_list = travel(rec_list)


    # Simuliere Infektionen mit Euler-Verfahren
    infectODEsolverAll(sus_list, inf_list, rec_list)
    print('Tag:', i)

for i in range(len(sus_list)):
    sus[i, 0] = sus_list[i]
    inf[i, 0] = inf_list[i]
    rec[i, 0] = rec_list[i]

create_map(sus_list, inf_list, rec_list)
