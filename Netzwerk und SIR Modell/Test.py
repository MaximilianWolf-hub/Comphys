import folium
from folium import IFrame
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Erstelle eine Beispielgrafik
def create_plot():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [10, 20, 25, 30])
    ax.set_title('Example Plot')

    # Speicher die Grafik in einem BytesIO-Objekt
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# Erstelle eine Folium-Karte
map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Erstelle die Grafik und encode sie in base64
plot_buf = create_plot()
plot_base64 = base64.b64encode(plot_buf.read()).decode('utf-8')
plot_buf.close()

# Erstelle ein HTML-iframe mit der Grafik
html = f'<img src="data:image/png;base64,{plot_base64}">'
iframe = IFrame(html, width=500, height=300)

# Füge einen Marker mit der Grafik hinzu
folium.Marker(
    [45.5236, -122.6750],
    popup=folium.Popup(iframe)
).add_to(map)

# Speichere die Karte als HTML-Datei
map.save('map_with_plot.html')