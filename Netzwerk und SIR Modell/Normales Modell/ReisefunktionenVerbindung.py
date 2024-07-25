from Städte_und_Populationen import population_combined, cities_combined

data = []

#Wir erstellen eine leere Liste, in welcher später die Reisemöglichkeiten zwischen den Städten gelistet werden.
#In der ersten Spalte ist eine Stadt vermerkt und in den restlichen Spalten einer Zeile die jeweils möglichen Reiseziele.

with open('allConnectionsCombined.txt', 'r', encoding='utf-8') as f:
    for line in f:
        entries = line.strip().split(',') #line.strip() entfernt Leerzeichen am Anfang und Ende der Zeile
                                          #split(',') teilt die Zeile in eine Liste von Einträgen, die durch Kommas getrennt sind.
                                          #Die erste Spalte stellt die Stadt dar, und die restlichen Spalten sind die möglichen Reiseziele.
        data.append(entries) #entries Liste wird zu Data hinzugefügt

#Die Funktion travel fasst alle Reisebewegungen zusammen, indem sie die Liste data mit ihren möglichen Reisebewegungen verwendet
#Durch Input einer Liste mit den jeweiligen Anzahlen an Infizierten/Suspekten/Genenesen können die Reisebewegungen schnell simuliert werden
def travelCombined(pop_list, pt):
    for i in range(len(pop_list)):  #Schleife iteriert über alle Einträge in der Pop-Liste
        pops = 0                    #Population alle möglichen Reiseziele einer Stadt
        for j in range(1, len(data[i][:])):  #Starte bei 1, da data[i][0] die aktuelle Stadt ist
            city_name = data[i][j]           #Stadt Name, zu der gereist werden kann wird gespeichert
            if city_name in cities_combined: #Wenn Stadt in cities_combined vorhanden ist
                index = cities_combined.index(city_name) #Index der Stadt wird gefunden
                pops += population_combined[index]       #Bevölkerung dieser Stadt wird zu pops addiert
        for k in range(1, len(data[i][:])):              #Hier werden jetzt die Reisen durch weitere Schleife in die
            city_name = data[i][k]                       #anderen Städte simuliert in die anderen Städte simuliert
            if city_name in cities_combined:
                index = cities_combined.index(city_name)
                pop_list[index] += (1 / pops) * pt * pop_list[i] * population_combined[index]  # eine Erklärung der Formel findet sich im Protokoll
                pop_list[i] -= (1 / pops) * pt * pop_list[i] * population_combined[index]
    return pop_list

