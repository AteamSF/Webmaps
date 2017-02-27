import folium

map = folium.Map(location = [38.889931,-77.009003],zoom_start = 12,tiles = 'Mapbox')
map.simple_marker(location = [38.897096,-77.036545],popup = 'White House', marker_color = 'red')
map.create_map(path = 'dc.html')
