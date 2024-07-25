from city_data import population as europa_population, cities as europa_cities

population_threshold = 2e6 #Definiere vorgegebenen Grenzwert für Flughäfen

Europa_large_airports = [city for city, pop in zip(europa_cities, europa_population) if pop > population_threshold]

#Es wird eine neue Liste erstellt, die alle europäischen Städte mit Flughafen enthält
#zip(europa_cities, europa_population) paart die Listen europa_cities und europa_population
#Die if Bedingung pop > population_threshold filtert die Städte heraus.

with open('large_airports_Europa.txt', 'w', encoding='utf-8') as file:
    for airport in Europa_large_airports:
        file.write(f'{airport}\n')

#Speichert die Flughäfen in einer Datei

