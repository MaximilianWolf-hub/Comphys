# Öffnen und Einlesen der Textdateien
with open('airConnections.txt', 'r') as file:
    europe_data = file.readlines()

with open('airConnectionsAfrica.txt', 'r') as file:
    africa_data = file.readlines()

# Öffnen und Einlesen der Verbindungen zwischen Europa und Afrika
with open('africa_europe_connections.txt', 'r') as file:
    africa_europe_data = file.readlines()

# Kombinieren der Daten
combined_data = europe_data + africa_data + africa_europe_data

# Speichern der kombinierten Verbindungen in einer neuen Datei
with open('combined_air_connections.txt', 'w') as file:
    file.writelines(combined_data)

# Ausgabe der ersten paar Zeilen, um sicherzustellen, dass alles korrekt zusammengeführt wurde
with open('combined_air_connections.txt', 'r') as file:
    print(file.readlines()[:5])
