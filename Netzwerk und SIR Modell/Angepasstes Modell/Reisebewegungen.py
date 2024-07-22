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
def travel(pop_list, pop, inf, rec, pt):
    for i in range(len(pop_list)):      #iteriert über alle Einträge in der Pop-liste
        pops = 0                        #Population alle möglichen Reiseziele einer Stadt
        for j in range(1, len(data[i][:])):  # Starte bei 1, da data[i][0] die aktuelle Stadt ist
            city_name = data[i][j]           # Berechne Einwohner in allen möglichen Reisezielen
            if city_name in cities:
                index = cities.index(city_name)
                pops += pop[index]
        for k in range(1, len(data[i][:])):  # hier werden jetzt die Reisen simuliert in die anderen Städte
            city_name = data[i][k]
            if city_name in cities:
                index = cities.index(city_name)
                if inf[index] / (pop[index]) >= 0.01:         # hier passen wir die Reisewahrscheinlichkeit an den Anteil der Infizierten an
                    pt_real = pt / 2                     # je mehr größer der Anteil an Infizierten, desto geringer die Reisewahrscheinlickeit
                else:
                    pt_real = pt / 1
                pop_list[index] += (1 / (pops)) * pt_real * pop_list[i] * pop[index]  # eine Erklärung der Formel findet sich im Protokoll
                pop_list[i] -= (1 / (pops)) * pt_real * pop_list[i] * pop[index]      # man beachte, wir verwenden nun die angepasste Reisewahrscheinlichkeit
    return pop_list

def travel_e(s_list, inf_list, rec_list, pt):
    for i in range(len(s_list)):
        if not inf_list[i] / (s_list[i] + rec_list[i]) >= 0.1:    #  wir ürüfen zuerst, ob nehr als 10% der Bevölkerung infiziert ist, wenn ja, gibt es zur Eindämmung der Epidemie keine Reisen aus dem Land raus
            pops = 0                                # es soll zunächst bestimmt werden, wie viel Einwohner in allen möglichen Reisezielen leben
            pt_real = pt * (0.1 - inf_list[i] / (s_list[i] +rec_list[i])) / 0.1       # die wahre Reisewahrscheinlichkeit ergibt sich durch die Annahme, dass je mehr Infizierte in einer Stadt sind, desto weniger wird gereist
            for j in range(1, len(data[i][:])):
                city_name = data[i][j]
                if city_name in cities:
                    index = cities.index(city_name)
                    pops += s_list[index] + rec_list[index]          # pops speichert gesunde Einwohner aller möglichen Reiseziele
            for k in range(1, len(data[i][:])):     #nun werden die Reisebewegungen realisiert
                city_name = data[i][k]
                if city_name in cities:
                    index = cities.index(city_name)
                    frac = (s_list[index] + rec_list[index]) / pops * pt_real
                    s_list[index] += s_list[i] * frac
                    s_list[i] -= s_list[i] * frac
                    rec_list[index] += rec_list[i] * frac
                    rec_list[i] -= rec_list[i] * frac
                    inf_list[index] += inf_list[i] * frac * (1 / 5)     # wir nehmen an, dass Infizierte weniger Reisen (hier Faktor 1 / 5)
                    inf_list[i] -= inf_list[i] * frac * (1 / 5)
