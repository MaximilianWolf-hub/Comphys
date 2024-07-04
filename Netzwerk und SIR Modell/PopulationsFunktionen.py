import numpy as np
from city_data import cities

landConnections = np.loadtxt("landConnections.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
airConnections = np.loadtxt("airConnections.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)

#Annahme die Änderung der Population innerhalb einer Stadt setzt sich zusammen aus Reisen
#aus anderen Städten in die jeweilige Stadt und Reisen aus der Stadt in andere Städte

#Reisewahrscheinlichkeit
pt = 0.01


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




def travelLandAll(pop_list):  #Reisebewegung an Land braucht Liste als Input um zwischen
                          #Reisebewegungen von Infizierten, Genesenen oder Suspects zu unterscheiden
    for i in cities:
        index = cities.index(i)
        L = travelLand(i)
        k = len(L)
        for j in L:
            index2 = cities.index(j)
            pop_list[index2] += 1 / k * pop_list[index] * pt
            pop_list[index] -= 1 / k * pop_list[index] * pt
    return pop_list

def travelAirAll(pop_list):         #Reisebewegung durch Luftverkehr braucht Liste als Input um zwischen
                                #Reisebewegungen von Infizierten, Genesenen oder Suspects zu unterscheiden
    for i in airConnections[:, 0]:
        index = cities.index(i)
        L = travelAir(i)
        k = len(L)
        if k > 0:  # Prüfe, ob es Verbindungen gibt
            for j in L:
                index2 = cities.index(j)
                pop_list[index2] += 1 / k * pop_list[index] * pt
                pop_list[index] -= 1 / k * pop_list[index] * pt
    return pop_list

