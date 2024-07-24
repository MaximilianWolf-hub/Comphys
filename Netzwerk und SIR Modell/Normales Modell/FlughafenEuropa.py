import numpy as np
from city_data import population as europa_population, cities as europa_cities

# Definieren Sie den Grenzwert für große Flughäfen
population_threshold = 2e6

# Finden Sie große Flughäfen in Afrika
Europa_large_airports = [city for city, pop in zip(europa_cities, europa_population) if pop > population_threshold]

# Speichern Sie die großen Flughäfen in einer Datei
with open('large_airports_Europa.txt', 'w', encoding='utf-8') as file:
    for airport in Europa_large_airports:
        file.write(f'{airport}\n')

print("Große Flughäfen in Europa gespeichert.")
