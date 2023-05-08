from pymongo import MongoClient
import pandas as pd
import time
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import geopandas as gpd

def create_heatmap(df):
    maps = folium.Map(location=[df['office latitude'].iloc[0], df['office longitude'].iloc[0]], zoom_start=2)

    heat_data = [[row['office latitude'], row['office longitude']] for index, row in df.iterrows() if row['office latitude'] is not None and row['office longitude'] is not None]
    HeatMap(heat_data).add_to(maps)

    return maps


def top3_map (final_cities):
    top3_cities_map = Map(location = [40, -99], zoom_start = 4)
    tech_group = folium.FeatureGroup(name=f"Tech ({final_cities[final_cities['type'] == 'tech'].shape[0]})")
    design_group = folium.FeatureGroup(name = f"Design ({final_cities[final_cities['type'] == 'design'].shape[0]})")

    for index, row in final_cities.iterrows():
        city = {
            "location": [row["office latitude"], row["office longitude"]],
            "tooltip": row["name"]
        }
        if row["type"] == "tech":
            icon = Icon (
                color = "blue",
                prefix="fa",
                icon="briefcase",
            )
        else:
            icon = Icon(
                color = "green",
                prefix="fa",
                icon="shirt"
            )   
        new_marker = Marker (**city, icon = icon)
        if row["type"] == "tech":
            new_marker.add_to(tech_group)
        else:
            new_marker.add_to(design_group)
    tech_group.add_to(top3_cities_map)
    design_group.add_to(top3_cities_map)
    folium.LayerControl(collapsed=False, position="topleft").add_to(top3_cities_map)
    return top3_cities_map



def markers (name, color, icon_, coordinates, map):
    icon1 = Icon(
    color = color,
    opacity = 0.1,
    prefix = "fa", 
    icon = icon_,
    icon_color = "white"
    )   
    marker_ = Marker(
    location = coordinates,
    tooltip = name,
    icon = icon1
    )
    marker_.add_to(map)
    return map