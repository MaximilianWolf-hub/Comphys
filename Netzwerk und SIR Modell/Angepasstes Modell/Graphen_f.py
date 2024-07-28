import numpy as np
import matplotlib.pyplot as plt
from SIR_f import infectODEsolverAll, sus, inf, rec, des, exp
from Reisebewegungen import travel
import time


# in diesem Modul wollen wir gezielt Plots von Populationsentwicklungen in einzelnen Städten erstellen

second_column_list = sus[:, 1].tolist()         # wir starten wie in main.py eine Infektion in London
index = second_column_list.index('LONDON')
inf[index, 0] = 1000            # anfang sind es 1000 Infizierte


sus_list = sus[:, 0].tolist()           # sus_list, inf_list und rec_list wie in main.py
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()
des_list = des[:, 0].tolist()
exp_list = exp[:, 0].tolist()

pt = 0.01       # Reisewahrscheinlichkeit


all_suspects = np.array([sus_list])      # enthalten wie in main.py die Populationsenticklungen aller Städte geordnet wie in cities
all_infections = np.array([inf_list])    # jede Spalte enthält die Populationsentwicklung einer Stadt
all_recovered = np.array([rec_list])
all_deceased = np.array([des_list])
all_exposed = np.array([exp_list])

start_time = time.time() # timer zur Beurteilung der Rechendauer

# Simulation über 365 Tage
for i in range(365):
    # Reisebewegungen simulieren
    sus_list = travel(sus_list, sus_list, inf_list, rec_list, pt)
    inf_list = travel(inf_list, sus_list, inf_list, rec_list, pt)
    rec_list = travel(rec_list, sus_list, inf_list, rec_list, pt)
    des_list = travel(des_list, sus_list, inf_list, rec_list, pt)
    exp_list = travel(exp_list, sus_list, inf_list, rec_list, pt)

    all_suspects = np.vstack((all_suspects, sus_list))
    all_infections = np.vstack((all_infections, inf_list))
    all_recovered = np.vstack((all_recovered, rec_list))
    all_deceased = np.vstack((all_deceased, des_list))
    all_exposed = np.vstack((all_exposed, exp_list))

    # Simuliere Infektionen mit gewünschten-Verfahren
    #infectEulerAll(sus_list, inf_list, rec_list)
    #infectRK4All(sus_list, inf_list, rec_list)
    infectODEsolverAll(sus_list, inf_list, rec_list, des_list, exp_list)
    print('Tag:', i)

end_time = time.time()
execution_time = end_time - start_time
print(f"Die Ausführungszeit beträgt: {execution_time} Sekunden")

# Graphische Darstellung der Populationen in London
plt.plot(all_suspects[:, index], label='S-Population')
plt.plot(all_infections[:, index], label='Infektionen')
plt.plot(all_recovered[:, index], label='Genesene')
plt.plot(all_deceased[:, index], label='Verstorbene')
plt.plot(all_exposed[:, index], label='Exponierte')
plt.yscale('log')
plt.ylabel('Anzahl an Personen')
plt.xlabel('Tage seit Infektionsbeginn')
plt.legend()
plt.title('Population London')
plt.savefig('noInfectedLondon.jpeg')
plt.show()


index2 = second_column_list.index('Frankfurt am Main')
# Graphische Darstellung der Populationen in Frankfurt am Main
plt.plot(all_suspects[:, index2], label='S-Population')
plt.plot(all_infections[:, index2], label='Infektionen')
plt.plot(all_recovered[:, index2], label='Genesene')
plt.plot(all_deceased[:, index2], label='Verstorbene')
plt.plot(all_exposed[:, index2], label='Exponierte')
plt.yscale('log')
plt.ylabel('Anzahl an Personen')
plt.xlabel('Tage seit Infektionsbeginn')
plt.legend()
plt.title('Population Frankfurt am Main')
plt.savefig('noInfectedFfm.jpeg')
plt.show()


#print('London Tag 30:', all_infections[30, index])
#print('London Tag 60:', all_infections[60, index])
#print('London Tag 150:', all_infections[150, index])
#print('London Tag 365:', all_infections[365, index])

