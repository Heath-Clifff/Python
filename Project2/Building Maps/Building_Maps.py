from folium import Popup
from branca.element import IFrame
import folium
import pandas as pd

volcanoes = pd.read_csv("Volcanoes.txt")

html = """<h4>Volcano information:</h4>
Height: %s m
"""


def colo_r(elev):
    if elev > 2000:
        return "red"
    else:
        return "green"


map = folium.Map(location=[48.7767982, -121.8109970],
                 zoom_start=4, tiles="Stamen Terrain")


fg = folium.FeatureGroup("Volcanoes")


for lat, lon, elev in zip(volcanoes['LAT'], volcanoes['LON'], list(volcanoes['ELEV'])):
    iframe = folium.IFrame(html=html % elev, width=200, height=100)
    fg.add_child(folium.Marker(

        location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color=colo_r(elev))))


fg1 = folium.FeatureGroup("Population")
fg1.add_child(folium.GeoJson(
    data=open("world.json", "r", encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'blue' if 10000000 < x['properties']['POP2005'] < 200000000 else 'red'}))


map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("Map1.html")
