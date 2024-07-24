import numpy as np

def read_city_data(file_path, min_population):
    data = np.loadtxt(file_path, delimiter='\t', dtype=str, encoding='utf-8', skiprows=1)

    h_staedte = data[:, 0]
    h_einwohner = data[:, 1].astype(float)
    h_laender = data[:, 2]
    h_breitengrad = data[:, 3].astype(float)
    h_laengengrad = data[:, 4].astype(float)

    cities = []
    population = []
    laender = []
    breitengrad = []
    laengengrad = []

    for i in range(len(h_einwohner)):
        if h_einwohner[i] >= min_population:
            cities.append(h_staedte[i])
            population.append(h_einwohner[i])
            laender.append(h_laender[i])
            breitengrad.append(h_breitengrad[i])
            laengengrad.append(h_laengengrad[i])

    return cities, population, laender, breitengrad, laengengrad

# Daten für Europa einlesen
cities_europe, population_europe, laender_europe, breitengrad_europe, laengengrad_europe = read_city_data('europe.csv',
                                                                                                          2e5)

# Daten für Afrika einlesen
cities_africa, population_africa, laender_africa, breitengrad_africa, laengengrad_africa = read_city_data('africa.csv',
                                                                                                          2e5)
# Kombinierte Daten erstellen
cities_combined = cities_europe + cities_africa
population_combined = population_europe + population_africa
laender_combined = laender_europe + laender_africa
breitengrad_combined = breitengrad_europe + breitengrad_africa
laengengrad_combined = laengengrad_europe + laengengrad_africa

print("Kombinierte Städte:", cities_combined)
print("Kombinierte Populationen:", population_combined)

#Einlesen der Verbindungen
landConnectionsCombined = np.loadtxt("combined_land_connections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnectionsCombined = np.loadtxt("combined_air_connections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

# Reisewahrscheinlichkeit
pt = 0.01

# Funktion gibt alle möglichen Land-Verbindungen aus als Liste
def travelLandCombined(city):
    L = []
    for i in range(len(landConnectionsCombined)):
        if city == landConnectionsCombined[i, 0]:
            L.append(landConnectionsCombined[i, 1])
        elif city == landConnectionsCombined[i, 1]:
            L.append(landConnectionsCombined[i, 0])
    return L

# Funktion gibt alle möglichen Luftverbindungen einer Stadt aus
def travelAirCombined(city):
    L = []
    for i in range(len(airConnectionsCombined)):
        if city == airConnectionsCombined[i, 0]:
            L.append(airConnectionsCombined[i, 1])
        elif city == airConnectionsCombined[i, 1]:
            L.append(airConnectionsCombined[i, 0])
    return L

# Funktion zur Simulation der Landreisebewegungen
def travelLandAllCombined(pop_list):
    for city in cities_combined:
        index = cities_combined.index(city)
        L = travelLandCombined(city)  # alle Landreiseziele
        total_pop = sum(population_combined[cities_combined.index(dest)] for dest in L)  # Summe der Einwohner der Landreiseziele
        if total_pop == 0:  # Vermeidung von Division durch Null
            continue
        for dest in L:
            index2 = cities_combined.index(dest)
            delta_pop = pt * pop_list[index] * population_combined[index2] / total_pop
            pop_list[index2] += delta_pop
            pop_list[index] -= delta_pop
    return pop_list

# Funktion zur Simulation der Luftreisebewegungen
def travelAirAllCombined(pop_list):
    for city in cities_combined:
        index = cities_combined.index(city)
        L = travelAirCombined(city)  # alle Luftreiseziele
        total_pop = sum(population_combined[cities_combined.index(dest)] for dest in L)  # Summe der Einwohner der Luftreiseziele
        if total_pop == 0:  # Vermeidung von Division durch Null
            continue
        for dest in L:
            index2 = cities_combined.index(dest)
            delta_pop = pt * pop_list[index] * population_combined[index2] / total_pop
            pop_list[index2] += delta_pop
            pop_list[index] -= delta_pop
    return pop_list

# Testen der Funktionen mit Beispieldaten
initial_population = population_combined.copy()
new_population_land = travelLandAllCombined(initial_population)
new_population_air = travelAirAllCombined(initial_population)

print("Population nach Landreisen:", new_population_land)
print("Population nach Luftreisen:", new_population_air)
