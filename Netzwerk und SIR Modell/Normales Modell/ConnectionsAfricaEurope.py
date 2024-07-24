# Funktion zum Einlesen der Flughäfen aus einer Datei
def read_airports(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        airports = [line.strip() for line in file.readlines()]
    return airports


# Einlesen der großen Flughäfen aus den Dateien
africa_large_airports = read_airports('large_airports_africa.txt')
europe_large_airports = read_airports('large_airports_Europa.txt')

# Erstellen Sie eine leere Liste für die neuen Verbindungen
connections_africa_europe = []

# Erstellen Sie Verbindungen zwischen großen Flughäfen
for africa_airport in africa_large_airports:
    for europe_airport in europe_large_airports:
        connections_africa_europe.append((africa_airport, europe_airport))

# Speichern Sie die Verbindungen in einer Datei
with open('africa_europe_connections.txt', 'w', encoding='utf-8') as file:
    # Überschrift hinzufügen
    ueberschrift = ['Stadt1', 'Stadt2']
    file.write(f'{ueberschrift[0]}\t{ueberschrift[1]}\n')

    # Verbindungen schreiben
    for connection in connections_africa_europe:
        file.write(f'{connection[0]}\t{connection[1]}\n')

print("Verbindungen zwischen Afrika und Europa gespeichert.")
