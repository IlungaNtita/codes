import folium

map=folium.Map(location=[-26.1714537,27.8999389], zoom_start=6, tiles = "Mapbox Bright")

map.add_child(folium.Marker(location=[-26.1714537,27.8999389],popup="Johannesburg", icon = folium.Icon(color="green")))

map.save("maps.html")