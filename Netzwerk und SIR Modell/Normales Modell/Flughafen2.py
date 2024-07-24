import numpy as np
from CityDataAfrica import population as africa_population, cities as africa_cities

# Definieren Sie den Grenzwert für große Flughäfen
population_threshold = 2e6

# Finden Sie große Flughäfen in Afrika
africa_large_airports = [city for city, pop in zip(africa_cities, africa_population) if pop > population_threshold]

# Speichern Sie die großen Flughäfen in einer Datei
with open('large_airports_africa.txt', 'w', encoding='utf-8') as file:
    for airport in africa_large_airports:
        file.write(f'{airport}\n')

print("Große Flughäfen in Afrika gespeichert.")
