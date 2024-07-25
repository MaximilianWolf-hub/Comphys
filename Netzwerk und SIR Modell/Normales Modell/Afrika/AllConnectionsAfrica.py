import numpy as np
from CityDataAfrica import cities, population

# Lade die Verbindungen
landConnectionsAfrica = np.loadtxt("../landConnectionsAfrica.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnectionsAfrica = np.loadtxt("../airConnectionsAfrica.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

# Funktion gibt alle möglichen Land-Verbindungen aus als Liste
def travelLandAfrica(city):
    L = []
    for i in range(len(landConnectionsAfrica)):
        if city == landConnectionsAfrica[i, 0]:
            L.append(landConnectionsAfrica[i, 1])
        elif city == landConnectionsAfrica[i, 1]:  # elif statt if, da beide Bedingungen nicht gleichzeitig zutreffen können
            L.append(landConnectionsAfrica[i, 0])
    return L

# Funktion gibt alle möglichen Luftverbindungen einer Stadt aus
def travelAirAfrica(city):
    L = []
    for i in range(len(airConnectionsAfrica)):
        if city == airConnectionsAfrica[i, 0]:
            L.append(airConnectionsAfrica[i, 1])
        elif city == airConnectionsAfrica[i, 1]:  # elif statt if, da beide Bedingungen nicht gleichzeitig zutreffen können
            L.append(airConnectionsAfrica[i, 0])
    return L

# In diesem File möchten wir den Vorgang etwas optimieren und berechnen im Voraus für jede Stadt die Luft- und Landverbindungen
# In der Datei allConnectionsAfrica.txt werden in einer Reihe jeweils die Stadt (1. Spalte) und all ihre Reiseverbindungen
# in der selben Reihe (also in den folgenden Spalten) hinzugefügt
# Wichtig: die einzelnen Städte sind durch Kommas abgetrennt, sodass Städte aus mehreren Wörtern später auch erkannt werden

with open('../allConnectionsAfrica.txt', 'w', encoding='utf-8') as datei:
    for i in range(len(cities)):
        city_name = cities[i]
        connections_str = travelLandAfrica(city_name)
        if population[i] > 1e6:
            connections_luft = travelAirAfrica(city_name)
            all_connections = ','.join(connections_str + connections_luft)
        else:
            all_connections = ','.join(connections_str)
        datei.write(f'{city_name},{all_connections}\n')
