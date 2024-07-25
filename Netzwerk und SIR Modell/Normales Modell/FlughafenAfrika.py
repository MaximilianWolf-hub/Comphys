from CityDataAfrica import population as africa_population, cities as africa_cities

population_threshold = 2e6  #Hier wird ein grenzwert für die Bevölkerung festgelegt, sodass nur Städte
                            #mit einer Bevölkerung von über 2 Millionen mit einem Flughafen registriert werden.

africa_large_airports = [city for city, pop in zip(africa_cities, africa_population) if pop > population_threshold]
#Es wird eine neue Liste erstellt, in der alle Städte mit Bevölkerung gespeichert werden, die den obigen grenzwert überschreiten.
#Die Zip Dunktion kombiniert die Listen africa_cities und africa_population paarweise. Danach folgt eine Schleife (for city), die
#city dem Städtenamen und pop der Bevölkerung zuweißt. Danch wird mit der if Bedingung überprüft, ob die Stadt mehr als 10^6 Einwohner hat,
#und fügt nur diese Städte hinzu.

with open('large_airports_africa.txt', 'w', encoding='utf-8') as file:  #Für jede Stadt in der vorherhig definierten Liste wird
    for airport in africa_large_airports:                               #der Name jeder stadt in eine neue Zeile geschrieben.
        file.write(f'{airport}\n')

print("Große Flughäfen in Afrika gespeichert.")
#Um zu sehen um welche Städte es sich handelt
