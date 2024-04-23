import folium
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd
import numpy as np  # Asegúrate de importar numpy

def plot_population_density_map(df):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]

    # Calculando percentiles para definir los bins
    percentiles = np.percentile(df_2023['Population density'], [10, 30, 50, 70, 90])
    print("Percentiles para bins:", percentiles)
    print(df_2023['Population density'].describe())  # Diagnóstico estadístico

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
        threshold_scale=list(percentiles),  # Utilizando percentiles como escalas
        nan_fill_color='white'  # Color para países sin datos
    ).add_to(m)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=False)
    )

    folium_static(m)