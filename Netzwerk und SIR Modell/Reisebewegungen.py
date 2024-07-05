from city_data import population, cities

#data wird alle Verbindungen enthalten, hierbei ist in der ersten Spalte die jeweilige Stadt vermerkt und in
#den restlichen Spalten einer Zeile die jeweils möglichen Reiseziele
data = []

#Reisewahrscheinlichkeit
pt = 0.01

with open('allConnections.txt', 'r', encoding='utf-8') as f:
    # Iteriere über jede Zeile in der Datei
    for line in f:
        # Entferne eventuelle Leerzeichen am Anfang und Ende der Zeile und teile sie in Einträge auf
        entries = line.strip().split(',')

        # Füge die Einträge dieser Zeile zur Datenliste hinzu
        data.append(entries)



#die Funktion travel fasst alle Reisebewegungen zusammen, indem sie die vorgefertigte Liste data mit ihren möglichen Reisebewegungen verwendet
#durch Input einer Liste mit den jeweiligen Anzahlen an Infizierten/Suspekten/Genenesen können die Reisebewegungen schnell simuliert werden
def travel(pop_list):
    for i in range(len(pop_list)):
        for j in range(1, len(data[i][:])):  # Starte bei 1, da data[i][0] die aktuelle Stadt ist
            city_name = data[i][j]
            if city_name in cities:
                index = cities.index(city_name)
                pop_list[index] += (1 / (len(data[i]) - 1)) * pt * pop_list[i]
                pop_list[i] -= (1 / (len(data[i]) - 1)) * pt * pop_list[i]
    return pop_list


