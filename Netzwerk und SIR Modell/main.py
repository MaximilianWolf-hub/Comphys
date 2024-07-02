import numpy as np
import matplotlib.pyplot as plt
from PopulationsFunktionen import travelLandAll, travelAirAll
from SIR_Funktionen import infectEulerAll, infectRK4All, infectODEsolverAll, sus, inf, rec


second_column_list = sus[:, 1].tolist()
index = second_column_list.index('LONDON')
inf[index, 0] = 1000


sus_list = sus[:, 0].tolist()
inf_list = inf[:, 0].tolist()
rec_list = rec[:, 0].tolist()
for i in range(10):
    sus_list = travelLandAll(sus_list)
    sus_list = travelAirAll(sus_list)
    inf_list = travelLandAll(inf_list)
    inf_list = travelAirAll(inf_list)
    rec_list = travelLandAll(rec_list)
    rec_list = travelAirAll(rec_list)

    sus_array = np.array(sus_list)
    inf_array = np.array(inf_list)
    rec_array = np.array(rec_list)

    infectRK4All(sus_list, inf_list, rec_list)

print(inf_list)


