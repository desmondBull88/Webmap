
import pandas
import folium


data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def colour_level(elev):
    if elev <= 1000:
        return 'lightgreen'
    elif elev > 1000 and elev < 3000:
        return 'green'
    else:
        return 'darkgreen'


map = folium.Map(location=[45.4215, -75.6972],
                 zoom_start=5, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='World Map')

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                                     popup=str(el)+' m', fill_color=colour_level(el), color='grey', fill_opacity=0.7))


fg.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000})))

map.add_child(fg)
map.save('WorldMap.html')
