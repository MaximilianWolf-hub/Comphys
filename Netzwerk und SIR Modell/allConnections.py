import numpy as np
from city_data import cities, population
from PopulationsFunktionen import travelLand, travelAir

landConnections = np.loadtxt("landConnections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnections = np.loadtxt("airConnections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)


#In diesem File möchten wir den Vorgang etwas optimieren und berechnen im Vorraus für jede Stadt die Luft und Lanverbindungen
#In der Datei allConnections.txt werden in einer Reihe jeweils die Stadt (1. Spalte) und all ihre Reiseverbindungen
#in der selben Reihe (also in den folgenden Spalten) hinzugefügt
#Wichtig: die einzelnen Städte sind durch Kommas abgetrennt, sodass Städte aus mehreren Wörten später auch erkannt werden
with open('allConnections.txt', 'w', encoding='utf-8') as datei:
    for i in range(len(cities)):
        if population[i] > 1e6:
            connections_luft = ','.join(travelAir(cities[i]))
            connections_str = ','.join(travelLand(cities[i]))
            datei.write(f'{cities[i]},{connections_str}\t{connections_luft}\n')
        else:
            connections_str = ','.join(travelLand(cities[i]))
            datei.write(f'{cities[i]},{connections_str}\n')





