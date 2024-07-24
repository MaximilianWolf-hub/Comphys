import numpy as np
from Städte_und_Populationen import cities_combined, population_combined

# Lade die Verbindungen
landConnectionsCombined = np.loadtxt("combined_land_connections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnectionsCombined = np.loadtxt("combined_air_connections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

# Funktion gibt alle möglichen Land-Verbindungen aus als Liste
def travelLandCombined(city):
    L = []
    for i in range(len(landConnectionsCombined)):
        if city == landConnectionsCombined[i, 0]:
            L.append(landConnectionsCombined[i, 1])
        elif city == landConnectionsCombined[i, 1]:  # elif statt if, da beide Bedingungen nicht gleichzeitig zutreffen können
            L.append(landConnectionsCombined[i, 0])
    return L

# Funktion gibt alle möglichen Luftverbindungen einer Stadt aus
def travelAirCombined(city):
    L = []
    for i in range(len(airConnectionsCombined)):
        if city == airConnectionsCombined[i, 0]:
            L.append(airConnectionsCombined[i, 1])
        elif city == airConnectionsCombined[i, 1]:  # elif statt if, da beide Bedingungen nicht gleichzeitig zutreffen können
            L.append(airConnectionsCombined[i, 0])
    return L

# In diesem File möchten wir den Vorgang etwas optimieren und berechnen im Voraus für jede Stadt die Luft- und Landverbindungen
# In der Datei allConnectionsAfrica.txt werden in einer Reihe jeweils die Stadt (1. Spalte) und all ihre Reiseverbindungen
# in der selben Reihe (also in den folgenden Spalten) hinzugefügt
# Wichtig: die einzelnen Städte sind durch Kommas abgetrennt, sodass Städte aus mehreren Wörtern später auch erkannt werden

with open('allConnectionsCombined.txt', 'w', encoding='utf-8') as datei:
    for i in range(len(cities_combined)):
        city_name = cities_combined[i]
        connections_str = travelLandCombined(city_name)
        if population_combined[i] > 1e6:
            connections_luft = travelAirCombined(city_name)
            all_connections = ','.join(connections_str + connections_luft)
        else:
            all_connections = ','.join(connections_str)
        datei.write(f'{city_name},{all_connections}\n')
