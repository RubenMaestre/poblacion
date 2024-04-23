import folium
from streamlit_folium import folium_static
import pandas as pd
import numpy as np

def plot_population_density_map(df):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]

    # Encuentra el mínimo y máximo en los datos
    min_density = df_2023['Population density'].min()
    max_density = df_2023['Population density'].max()

    # Crear bins que cubran todo el rango de datos
    bins = np.linspace(min_density, max_density, num=6)  # Crea 5 intervalos desde el mínimo al máximo

    m = folium.Map(location=[20, 0], tiles="cartodbpositron", zoom_start=2, width='100%', height='80%')

    choropleth = folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        name='choropleth',
        data=df_2023,
        columns=['Code', 'Population density'],
        key_on='feature.id',
        fill_color='YlOrRd',  # Amarillo a Rojo
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Densidad de población (personas por km²)',
        threshold_scale=list(bins),  # Usa los bins ajustados
        nan_fill_color='white'  # Color para países sin datos
    ).add_to(m)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=False)
    )

    folium_static(m)