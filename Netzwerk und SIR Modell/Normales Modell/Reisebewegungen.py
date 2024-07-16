from city_data import population, cities

#data wird alle Verbindungen enthalten, hierbei ist in der ersten Spalte die jeweilige Stadt vermerkt und in
#den restlichen Spalten einer Zeile die jeweils möglichen Reiseziele
data = []

#Reisewahrscheinlichkeit

with open('allConnections.txt', 'r', encoding='utf-8') as f: #daten sind mit Komma getrennt
    # Iteriere über jede Zeile in der Datei
    for line in f:
        # Entferne eventuelle Leerzeichen am Anfang und Ende der Zeile und teile sie in Einträge auf
        entries = line.strip().split(',')

        # Füge die Einträge dieser Zeile zur Datenliste hinzu
        data.append(entries)



#die Funktion travel fasst alle Reisebewegungen zusammen, indem sie die vorgefertigte Liste data mit ihren möglichen Reisebewegungen verwendet
#durch Input einer Liste mit den jeweiligen Anzahlen an Infizierten/Suspekten/Genenesen können die Reisebewegungen schnell simuliert werden
def travel(pop_list, pt):
    for i in range(len(pop_list)):      #iteriert über alle Einträge in der Pop-liste
        pops = 0                        #Population alle möglichen Reiseziele einer Stadt
        for j in range(1, len(data[i][:])):  # Starte bei 1, da data[i][0] die aktuelle Stadt ist
            city_name = data[i][j]           # Berechne Einwohner in allen möglichen Reisezielen
            if city_name in cities:
                index = cities.index(city_name)
                pops += population[index]
        for k in range(1, len(data[i][:])):  # hier werden jetzt die Reisen simuliert in die anderen Städte
            city_name = data[i][k]
            if city_name in cities:
                index = cities.index(city_name)
                pop_list[index] += (1 / (pops)) * pt * pop_list[i] * population[index]  # eine Erklärung der Formel findet sich im Protokoll
                pop_list[i] -= (1 / (pops)) * pt * pop_list[i] * population[index]
    return pop_list


def travel_new(s_list, inf_list, rec_list, pt):
    for i in range(len(s_list)):
        pops = 0                                 #Population alle möglichen Reiseziele einer Stadt
        for j in range(1, len(data[i][:])):
            city_name = data[i][j]
            if city_name in cities:
                index = cities.index(city_name)
                pops += s_list[index]           # pops speichert gesunde Einwohner aller möglichen Reiseziele
        for k in range(1, len(data[i][:])):     #nun werden die Reisebewegungen realisiert
            city_name = data[i][k]
            if city_name in cities:
                index = cities.index(city_name)
                s_list[index] += (1 / (pops)) * pt * s_list[i] * s_list[index]
                s_list[i] -= (1 / (pops)) * pt * s_list[i] * s_list[index]
                rec_list[index] += (1 / (pops)) * pt * s_list[index] * rec_list[i]  # eine Erklärung der Formel findet sich im Protokoll
                rec_list[i] -= (1 / (pops)) * pt * s_list[index] * rec_list[i]
                inf_list[index] += (1 / (pops)) * pt * s_list[index] * inf_list[i]
                inf_list[i] -= (1 / (pops)) * pt * s_list[index] * inf_list[i]
