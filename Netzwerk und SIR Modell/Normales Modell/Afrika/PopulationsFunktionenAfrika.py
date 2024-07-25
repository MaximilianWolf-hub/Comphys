import numpy as np
from CityDataAfrica import cities, population

# Lade die Verbindungen
landConnectionsAfrica = np.loadtxt("../landConnectionsAfrica.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnectionsAfrica = np.loadtxt("../airConnectionsAfrica.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

# Annahme: die Änderung der Population innerhalb einer Stadt setzt sich zusammen aus Reisen
# aus anderen Städten in die jeweilige Stadt und Reisen aus der Stadt in andere Städte

# Reisewahrscheinlichkeit
pt = 0.01

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

# Funktion zur Simulation der Landreisebewegungen
def travelLandAfricaAll(pop_list):
    for city in cities:
        index = cities.index(city)
        L = travelLandAfrica(city)  # alle Landreiseziele
        total_pop = sum(population[cities.index(dest)] for dest in L)  # Summe der Einwohner der Landreiseziele
        if total_pop == 0:  # Vermeidung von Division durch Null
            continue
        for dest in L:
            index2 = cities.index(dest)
            delta_pop = pt * pop_list[index] * population[index2] / total_pop
            pop_list[index2] += delta_pop
            pop_list[index] -= delta_pop
    return pop_list

# Funktion zur Simulation der Luftreisebewegungen
def travelAirAfricaAll(pop_list):
    for city in airConnectionsAfrica[:, 0]:
        index = cities.index(city)
        L = travelAirAfrica(city)  # alle Luftreiseziele
        total_pop = sum(population[cities.index(dest)] for dest in L)  # Summe der Einwohner der Luftreiseziele
        if total_pop == 0:  # Vermeidung von Division durch Null
            continue
        for dest in L:
            index2 = cities.index(dest)
            delta_pop = pt * pop_list[index] * population[index2] / total_pop
            pop_list[index2] += delta_pop
            pop_list[index] -= delta_pop
    return pop_list
