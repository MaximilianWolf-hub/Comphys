import folium
from Städte_und_Populationen import cities_combined, breitengrad_combined, laengengrad_combined
import matplotlib.pyplot as plt
from folium import IFrame
import base64
from io import BytesIO

def create_plot(sus, inf, rec, name):        #Wir erstellen für jede Stadt einen interaktiven Plot
    fig, ax = plt.subplots()                 #dieser wird dann encoded und in unsere Karte
    ax.plot(sus, label='S-Population') #an der richtigen Stelle eingefügt
    ax.plot(inf, label='Infiziert')
    ax.plot(rec, label='Genesen')
    plt.xlabel('Tage seit Infektionsbeginn')
    plt.ylabel('Gesamtzahl Personen')
    plt.yscale('log')
    ax.set_title(name)
    ax.legend()

    buf = BytesIO()                   # Speicher die Grafik in einem BytesIO-Objekt
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)                    # Schließe die Figur, um Speicher zu sparen
    return buf

def encode(sus, inf, rec, name):                     #encode Funktion kodiert Daten in base64,
    plot_buf = create_plot(sus, inf, rec, name)      #um es später als HTML-Image darstellen zu können
    plot_base64 = base64.b64encode(plot_buf.read()).decode('utf-8')
    plot_buf.close()

    # Erstelle ein HTML-iframe mit der Grafik
    html = f'<img src="data:image/png;base64,{plot_base64}">'
    iframe = IFrame(html, width=500, height=300)
    return iframe

def create_map(sus, inf, rec):
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)  #zentriert auf Deutschland

    #Erstellen einer Liste mit allen wichtigen Parametern einer Stadt
    data = []
    for i in range(len(cities_combined)):
        data.append({
            'name': cities_combined[i],
            'Breitengrad': breitengrad_combined[i],
            'Längengrad': laengengrad_combined[i],
            'S-population': sus[:, i],
            'Infizierte': inf[:, i],
            'Genesene': rec[:, i]
        })

    #Hinzufügen von Markern zur Karte
    for city in data:
        folium.Marker(
            location=[city['Breitengrad'], city['Längengrad']],
            popup=folium.Popup(encode(city['S-population'], city['Infizierte'], city['Genesene'], city['name']), max_width=300),
            tooltip=city['name']
        ).add_to(m)

    #Karte speichern
    m.save('map_SIR_AfEu.html')  # Name der HTML-Datei

