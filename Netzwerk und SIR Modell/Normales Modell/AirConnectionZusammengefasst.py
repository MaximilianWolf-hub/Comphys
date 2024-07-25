with open('airConnections.txt', 'r') as file: #öffnet Datei und liest sie in Liste ein
    europe_data = file.readlines()

with open('airConnectionsAfrica.txt', 'r') as file: #Öffnet und Einlesen der Datei in liste
    africa_data = file.readlines()

with open('africa_europe_connections.txt', 'r') as file: # Öffnen und Einlesen der Verbindungen zwischen Europa und Afrika
    africa_europe_data = file.readlines()

combined_data = europe_data + africa_data + africa_europe_data # Kombinieren der Daten

with open('combined_air_connections.txt', 'w') as file: #speichert neue Verbindungen in einer neuen Datei namens combined_data
    file.writelines(combined_data)


