import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('europe.csv', delimiter='\t', dtype=str, encoding='utf-8', skiprows=1)

staedte = data[:, 0]
einwohner = data[:, 1].astype(float)
laender = data[:, 2]
breitengrad = data[:, 3].astype(float)
laengengrad = data[:, 4].astype(float)

#Listen wobei dort nur Städte mit mehr als 2 * 10^5 Einwohner berücksichtigt werden
g_staedte = []
g_einwohner = []
g_laender = []
g_breitengrad = []
g_laengengrad = []

for i in range(len(einwohner)):
    if einwohner[i] >= 2e5:
        g_einwohner.append(einwohner[i])
        g_laender.append(laender[i])
        g_breitengrad.append(breitengrad[i])
        g_laengengrad.append(laengengrad[i])
        g_staedte.append(staedte[i])


def abstand(j, k): #berechnet Abstand in Kilometer
    dx = 71.5 * (g_laengengrad[j] - g_laengengrad[k])  #71,5 km ist Abstand zwischen zwei Längengraden
    dy = 111.3 * (g_breitengrad[j] - g_breitengrad[k]) #111,3 km ist Abstand zweier Längengrade
    return np.sqrt(dx**2 + dy**2)

with open('landverkehr.txt', 'w', encoding='utf-8') as file:
    ueberschrift = ['Stadt1', 'Stadt2', 'Abstand']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\t{ueberschrift[2]}\n')
    for i in range(len(g_staedte)):
        for j in range(i + 1, len(g_staedte)):  # Starten bei i+1, um doppelte Berechnung zu vermeiden
            abstand_ij = abstand(i, j)
            if abstand_ij <= 500:
                file.write(f'{g_staedte[i]}\t{g_staedte[j]}\t{abstand_ij:.2f}\n')

with open('flugverkehr', 'w', encoding='utf-8') as file:
    ueberschrift = ['Stadt1', 'Stadt2']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\n')
    for i in range(len(g_staedte)):
        if g_einwohner[i] >= 1e6:
            for j in range(i + 1, len(g_staedte)):
                if g_einwohner[j] >= 1e6:
                    file.write(f'{g_staedte[i]}\t{g_staedte[j]}\n')

