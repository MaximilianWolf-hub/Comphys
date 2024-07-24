import numpy as np

# Wir lesen die vorgegebene Datei africa.csv ein und sortieren die Daten in Listen
data = np.loadtxt('africa.csv', delimiter='\t', dtype=str, encoding='utf-8', skiprows=1)

h_staedte = data[:, 0]
h_einwohner = data[:, 1].astype(float)
h_laender = data[:, 2]
h_breitengrad = data[:, 3].astype(float)
h_laengengrad = data[:, 4].astype(float)

# Listen der Städte, wobei dort nur Städte mit mehr als 2 * 10^5 Einwohner berücksichtigt werden
cities = []
population = []
laender = []
breitengrad = []
laengengrad = []

for i in range(len(h_einwohner)):  # hier prüfen wir, welche Städte mehr als 2 * 10^5 Einwohner haben und damit untersucht werden
    if h_einwohner[i] >= 2e5:
        population.append(h_einwohner[i])
        laender.append(h_laender[i])
        breitengrad.append(h_breitengrad[i])
        laengengrad.append(h_laengengrad[i])
        cities.append(h_staedte[i])


def abstand(j, k):  # berechnet Abstand zweier Städte in Kilometern
    dx = 71.5 * (laengengrad[j] - laengengrad[k])  # 71,5 km ist Abstand zwischen zwei Längengraden
    dy = 111.3 * (breitengrad[j] - breitengrad[k])  # 111,3 km ist Abstand zweier Breitengrade
    return np.sqrt(dx**2 + dy**2)


# Speichert alle Land- und Luftverbindungen in jeweils einer Textdatei, auf welche zugegriffen werden kann
with open('landConnectionsAfrica.txt', 'w', encoding='utf-8') as file:
    ueberschrift = ['Stadt1', 'Stadt2', 'Abstand']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\t{ueberschrift[2]}\n')
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):  # Starten bei i+1, um doppelte Berechnung zu vermeiden
            abstand_ij = abstand(i, j)
            if abstand_ij <= 500:  # alle möglichen Landverbindungen, also alle Städte, die näher als 500 km voneinander entfernt sind, kommen in die Textdatei landConnectionsAfrica.txt
                file.write(f'{cities[i]}\t{cities[j]}\t{abstand_ij:.2f}\n')

with open('airConnectionsAfrica.txt', 'w', encoding='utf-8') as file:
    ueberschrift = ['Stadt1', 'Stadt2']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\n')
    for i in range(len(cities)):
        if population[i] >= 1e6:  # alle Städte mit mehr als 1 Mio. Einwohner kommen in die Luftverbindungsdatei
            for j in range(i+1, len(cities)):
                if population[j] >= 1e6:
                    file.write(f'{cities[i]}\t{cities[j]}\n')

print(cities)
