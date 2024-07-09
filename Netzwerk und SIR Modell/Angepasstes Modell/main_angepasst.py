from SIR_angepasst import infectODEsolverAll, sus, inf, rec, vac
from Reisebewegungen import travel
from Europakarte_angepasst import create_map


second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON')
inf[index, 0] = 1000


sus_list = sus[:, 0].tolist()
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()
vac_list = vac[:, 0].tolist()



pt = 0.01



# Simulation über 365 Tage
for i in range(60):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list, pt)
    inf_list = travel(inf_list, pt)
    rec_list = travel(rec_list, pt)
    vac_list = travel(vac_list, pt)


    # Simuliere Infektionen mit Euler-Verfahren
    infectODEsolverAll(sus_list, inf_list, rec_list, vac_list)
    print('Tag:', i)

for i in range(len(sus_list)):
    sus[i, 0] = sus_list[i]
    inf[i, 0] = inf_list[i]
    rec[i, 0] = rec_list[i]
    vac[i, 0] = vac_list[i]

#Erstelle Karte mit Daten nach geüwnschtem Zeitraum
create_map(sus_list, inf_list, rec_list, vac_list)
