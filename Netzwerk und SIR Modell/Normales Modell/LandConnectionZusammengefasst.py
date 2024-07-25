with open('landConnections.txt', 'r') as file:  #öffnet und liest landConnections von europa ein und
    europe_data = file.readlines()              #speichert Daten in europe_data Liste

with open('landConnectionsAfrica.txt', 'r') as file: #öffnet und liest landConnections von Afrika ein und
    africa_data = file.readlines()                   #speichert Daten in africa_data Liste

combined_data = europe_data + africa_data   #kombiniert beide Listen zu einer

with open('combined_land_connections.txt', 'w') as file:  #Speichert die kombinierten Verbindungen
    file.writelines(combined_data)                        #in einer neuen Datei
