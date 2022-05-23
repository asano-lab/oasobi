import platform
import os
import folium

pf = platform.system()

print(pf)

print(os.getenv("PATH"))

folium.Marker()
