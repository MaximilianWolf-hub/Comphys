import folium
from CityDataAfrica import cities as africa_cities, breitengrad as africa_breitengrad, \
    laengengrad as africa_laengengrad
from CityDataEurope import cities as europe_cities, breitengrad as europe_breitengrad, \
    laengengrad as europe_laengengrad
from folium import IFrame
import base64
from io import BytesIO


def create_plot(sus, inf, rec, name):
    fig, ax = plt.subplots()
    ax.plot(sus, label='S-Population')
    ax.plot(inf, label='Infiziert')
    ax.plot(rec, label='Genesen')
    plt.xlabel('Tage seit Infektionsbeginn')
    plt.ylabel('Gesamtzahl Personen')
    ax.set_title(name)
    ax.legend()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf


def encode(sus, inf, rec, name):
    plot_buf = create_plot(sus, inf, rec, name)
    plot_base64 = base64.b64encode(plot_buf.read()).decode('utf-8')
    plot_buf.close()

    html = f'<img src="data:image/png;base64,{plot_base64}">'
    iframe = IFrame(html, width=500, height=300)
    return iframe


def create_map(sus, inf, rec):
    m = folium.Map(location=[20.0, 0.0], zoom_start=2)  # Zentrum auf die Weltkarte

    # Erstellen von Kartenmarkern für Afrika
    for i in range(len(africa_cities)):
        folium.Marker(
            location=[africa_breitengrad[i], africa_laengengrad[i]],
            popup=folium.Popup(encode(sus[:, i], inf[:, i], rec[:, i], africa_cities[i]), max_width=300),
            tooltip=africa_cities[i]
        ).add_to(m)

    # Erstellen von Kartenmarkern für Europa
    for i in range(len(europe_cities)):
        folium.Marker(
            location=[europe_breitengrad[i], europe_laengengrad[i]],
            popup=folium.Popup(encode(sus[:, i], inf[:, i], rec[:, i], europe_cities[i]), max_width=300),
            tooltip=europe_cities[i]
        ).add_to(m)

    # Verbindungen zwischen großen Flughäfen
    with open('africa_europe_connections.txt', 'r') as file:
        for line in file:
            city1, city2 = line.strip().split(',')
            loc1 = None
            loc2 = None
            for i in range(len(africa_cities)):
                if africa_cities[i] == city1:
                    loc1 = [africa_breitengrad[i], africa_laengengrad[i]]
                if africa_cities[i] == city2:
                    loc2 = [africa_breitengrad[i], africa_laengengrad[i]]
            if loc1 and loc2:
                folium.PolyLine(locations=[loc1, loc2], color='blue', weight=2.5, opacity=1).add_to(m)
            else:
                for i in range(len(europe_cities)):
                    if europe_cities[i] == city1:
                        loc1 = [europe_breitengrad[i], europe_laengengrad[i]]
                    if europe_cities[i] == city2:
                        loc2 = [europe_breitengrad[i], europe_laengengrad[i]]
                if loc1 and loc2:
                    folium.PolyLine(locations=[loc1, loc2], color='blue', weight=2.5, opacity=1).add_to(m)

    m.save('map_Africa_Europe.html')


# Beispielaufruf der Funktion zum Erstellen der Karte
create_map(all_suspects, all_infections, all_recovered)
