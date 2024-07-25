def read_airports(filename): # Funktion zum Einlesen der Flughäfen aus einer Datei
    with open(filename, 'r', encoding='utf-8') as file:
        airports = [line.strip() for line in file.readlines()]
    return airports
#Alle Städte mit Flughafen werden in der Liste airports gespeichert, die dann zurückgegeben wird.

africa_large_airports = read_airports('large_airports_africa.txt') #Flughäfen werden aus den Dateien eingelesen
europe_large_airports = read_airports('large_airports_Europa.txt')

connections_africa_europe = [] #Neue Liste für Flugverbindungen

for africa_airport in africa_large_airports:
    for europe_airport in europe_large_airports:
        connections_africa_europe.append((africa_airport, europe_airport))

#Die beiden schleifen duchlaufen jede Kombination von Flughäfen aus Afrika
#und Europa und fügt diese der Liste connections_africa_europe hinzu.

with open('africa_europe_connections.txt', 'w', encoding='utf-8') as file:
    ueberschrift = ['Stadt1', 'Stadt2']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\n')

    for connection in connections_africa_europe:
        file.write(f'{connection[0]}\t{connection[1]}\n')

#jede verbindung aus der Liste wird in der Datei connections_africa_europe gespeichert.