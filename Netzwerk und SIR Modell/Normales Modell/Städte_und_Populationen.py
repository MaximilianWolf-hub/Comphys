import numpy as np

def read_city_data(file_path, min_population):
    data = np.loadtxt(file_path, delimiter='\t', dtype=str, encoding='utf-8', skiprows=1)
#read_city_data Funktion liest die einzelnen Daten von Städten aus einer Datei ein. Die Funktion beachtet die zwei Parameter:
#file_path (der Pfad zur Datei) und min_population (die Mindestbevölkerungszahl, um berücksichtigt zu werden). Dabei werden durch
#dtype=str alle Daten als String interpretiert und durch skiprows die erste Zeile der Datei übersprungen, da diese die überschriften enthält.

    h_staedte = data[:, 0]
    h_einwohner = data[:, 1].astype(float)
    h_laender = data[:, 2]
    h_breitengrad = data[:, 3].astype(float)
    h_laengengrad = data[:, 4].astype(float)

#Die Daten aus der read_city_data Funktion werden in die 5 verschiedenen Arrays aufgeteilt.

    cities = []
    population = []
    laender = []
    breitengrad = []
    laengengrad = []

#Es werden leere Listen für die Daten erstellt.

    for i in range(len(h_einwohner)):
        if h_einwohner[i] >= min_population:
            cities.append(h_staedte[i])
            population.append(h_einwohner[i])
            laender.append(h_laender[i])
            breitengrad.append(h_breitengrad[i])
            laengengrad.append(h_laengengrad[i])

    return cities, population, laender, breitengrad, laengengrad

#Die Schleife iteriert über die Einwohnerzahlen und fügt dabei nur die Städte hinzu, die eine
#Bevölkerung haben, die Größer als min_population ist. Durch return werden die gefilterten Daten in
# die leeren Listen zurückgegeben.

cities_europe, population_europe, laender_europe, breitengrad_europe, laengengrad_europe = read_city_data('europe.csv',
                                                                                                          2e5)
cities_africa, population_africa, laender_africa, breitengrad_africa, laengengrad_africa = read_city_data('africa.csv',
                                                                                                          2e5)
#Es werden die Daten von der Europa.csv und der Afrika.csv Datei von der read_city_data funktion eingelesen.
#Dabei beachtet die Funktion, dass jeweils eine Mindestbevölkerung von 200.000 erreicht ist.

cities_combined = cities_europe + cities_africa
population_combined = population_europe + population_africa
laender_combined = laender_europe + laender_africa
breitengrad_combined = breitengrad_europe + breitengrad_africa
laengengrad_combined = laengengrad_europe + laengengrad_africa

#Die eingelesenen Daten werden zu jeweils einer Liste kombiniert

print("Kombinierte Städte:", cities_combined)
print("Kombinierte Populationen:", population_combined)

landConnectionsCombined = np.loadtxt("combined_land_connections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnectionsCombined = np.loadtxt("combined_air_connections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)
#Die Land- und Luftverbindungen werden aus den Dateien combined_land_connections.txt und combined_air_connections.txt eingelesen.

pt = 0.01   #Reisewahrscheinlichkeit

def travelLandCombined(city):
    L = []
    for i in range(len(landConnectionsCombined)):
        if city == landConnectionsCombined[i, 0]:
            L.append(landConnectionsCombined[i, 1])
        elif city == landConnectionsCombined[i, 1]:
            L.append(landConnectionsCombined[i, 0])
    return L

#Die travelLandCombined Funktion gibt alle möglichen Landverbindungen einer Stadt als Liste zurück. dabei ist city der Parameter,
#also der name der Stadt, für die die verbindungen gesucht werden soll. Es wird eine leere Liste L erzeugt, in der die Verbindungen
#eingefügt werden. Die Schleife durchläuft alle Einträge der Liste landConnectionsCombined (Liste von 2D-Arrays) und überprüft, ob der
#Parameter city der erste in der verbindung ist und fügt im Fall diese in die Liste hinzu. Die elif-Bedingung überprüft, ob der Parameter
#an zweiter Stelle steht und fügt die erste in die Liste hinzu.

def travelAirCombined(city):
    L = []
    for i in range(len(airConnectionsCombined)):
        if city == airConnectionsCombined[i, 0]:
            L.append(airConnectionsCombined[i, 1])
        elif city == airConnectionsCombined[i, 1]:
            L.append(airConnectionsCombined[i, 0])
    return L

# Funktion gibt alle möglichen Luftverbindungen einer Stadt aus, mit der gleichen Schleife wie oben.

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

# In diesem File möchten wir den Vorgang etwas optimieren und berechnen im Voraus für jede Stadt die Luft- und Landverbindungen
# In der Datei allConnectionsAfrica.txt werden in einer Reihe jeweils die Stadt (1. Spalte) und all ihre Reiseverbindungen
# in der selben Reihe (also in den folgenden Spalten) hinzugefügt
# Wichtig: die einzelnen Städte sind durch Kommas abgetrennt, sodass Städte aus mehreren Wörtern später auch erkannt werden

def travelLandAllCombined(pop_list):
    for city in cities_combined:
        index = cities_combined.index(city) #Schleife iteriert über alle Städte, und gibt Stadt index, um auf Bevölkerungszahl der Stadt in pop_list und population_combined zuzugreifen
        L = travelLandCombined(city)  #alle Landreiseziele
        total_pop = sum(population_combined[cities_combined.index(dest)] for dest in L)  #Summe der Einwohner der Landreiseziele
        if total_pop == 0:  #Vermeidung von Division durch Null, falls keine Bevölkerung in Stadt vorhanden ist
            continue
        for dest in L:
            index2 = cities_combined.index(dest) #ermittelt für jede verbundene Stadt index
            delta_pop = pt * pop_list[index] * population_combined[index2] / total_pop
            pop_list[index2] += delta_pop
            pop_list[index] -= delta_pop
    return pop_list

#Durch die travelLandAllCombined Funktion wird für jede Stadt die Bevölkerung gleichmäßig auf die verbundenen Städte verteilt.
#Die Funktion hat den Parameter pop_list, welche eine Liste von Bevölkerungszahlen ausgibt, die die aktuelle Bevölkerung jeder Stadt in
#cities_combined repräsentiert.
#delta_pop ist die Anzahl der Menschen, die von der Stadt (city) zur verbundenen Stadt (dest) reisen.
#Die Bevölkerung der verbundenen Stadt wird um delta_pop erhöht und die Bevölkerung der aktuellen Stadt wird um delta_pop verringert, da Menschen von
#einer Stadt in eine andere reisen, und dadurch die Bevölkerung der Abreisestadt abnimmt und die Bevölkerung der verbundenen Stadt zunimmt.

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
#Die travelAirAllCombined funktion funktioniert wie die travelLandAllCombined Funktion.

initial_population = population_combined.copy()
new_population_land = travelLandAllCombined(initial_population)
new_population_air = travelAirAllCombined(initial_population)

#Test der funktionen

print("Population nach Landreisen:", new_population_land)
print("Population nach Luftreisen:", new_population_air)
