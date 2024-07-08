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
        city_name = cities[i]
        if population[i] > 1e6:
            connections_luft = travelAir(city_name)
            connections_str = travelLand(city_name)
            all_connections = ','.join(connections_str + connections_luft)
            datei.write(f'{city_name},{all_connections}\n')
        else:
            connections_str = travelLand(city_name)
            all_connections = ','.join(connections_str)
            datei.write(f'{city_name},{all_connections}\n')





