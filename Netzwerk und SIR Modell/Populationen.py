import numpy as np
from city_data import cities, population, laender, breitengrad, laengengrad

landConnections = np.loadtxt("landConnections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnections = np.loadtxt("airConnections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

#Annahme die Änderung der Population innerhalb einer Stadt setzt sich zusammen aus Reisen
#aus anderen Städten in die jeweilige Stadt und Reisen aus der Stadt in andere Städte

#Reisewahrscheinlichkeit
pt = 1e-5


#Funktion gibt alle möglichen Land-Verbindungen aus als Liste
def travelLand(city):
    L = []
    for i in range(len(landConnections)):
        if city == landConnections[i, 0]:
            L.append(landConnections[i, 1])
        if city == landConnections[i, 1]:
            L.append(landConnections[i, 0])
    return L


#Funktion gibt alle möglichen Luftverbindungen einer Stand aus
def travelAir(city):
    if city in airConnections:
        L = []
        for i in range(len(airConnections)):
            if city == airConnections[i, 0]:
                L.append(airConnections[i, 1])
            if city == airConnections[i, 1]:
                L.append(airConnections[i, 0])
        return L
    else:
        return []
