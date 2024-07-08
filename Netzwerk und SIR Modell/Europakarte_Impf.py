import folium
from city_data import cities, breitengrad, laengengrad


def create_map(sus, inf, rec, vac):
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)  # Deutschland, zentriert

    # Erstellen einer Liste mit allen wichtigen Parametern einer Stadt
    data = []
    for i in range(len(cities)):
        data.append({
            'name': cities[i],
            'Breitengrad': breitengrad[i],
            'Längengrad': laengengrad[i],
            'S-Population': sus[i],
            'Infizierte': inf[i],
            'Genesene': rec[i],
            'Geimpfte': vac[i]
        })

    # Hinzufügen von Markern zur Karte
    for city in data:
        folium.Marker(
            location=[city['Breitengrad'], city['Längengrad']],
            popup=(
                f"<strong>{city['name']}</strong><br>"
                f"S-Population: {city['S-Population']}<br>"
                f"Infizierte: {city['Infizierte']}<br>"
                f"Genesene: {city['Genesene']}"
                f"Geimpfte: {city['Geimpfte']}"
            ),
            tooltip=city['name']
        ).add_to(m)

    # Karte speichern
    m.save('map_with_vaccination.html')



