import numpy as np
import matplotlib.pyplot as plt
from SIR_Funktionen import infectODEsolverAll, sus, inf, rec, infectRK4All, infectEulerAll
from Reisebewegungen import travel



second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON')
inf[index, 0] = 0


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
    infectRK4All(sus_list, inf_list, rec_list)
    print('Tag:', i)

plt.plot(all_suspects[:, index], label='S-Population')
plt.plot(all_infections[:, index], label='Infektionen')
plt.plot(all_recovered[:, index], label='Genesene')
plt.yscale('log')
plt.ylabel('Anzahl an Personen')
plt.xlabel('Tage seit Infektionsbeginn')
plt.legend()
plt.savefig('SIR_normal_rk4.jpeg')
plt.show()


