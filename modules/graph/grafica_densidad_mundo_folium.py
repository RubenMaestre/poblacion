import folium
import pandas as pd
import numpy as np
import branca.colormap as cm

def plot_population_density_map_with_folium(df, width=1200, height=500):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]
    
    # Utiliza los valores reales de densidad de población
    min_density = df_2023['Population density'].min()
    max_density = df_2023['Population density'].max()

    # Define una escala de colores
    colormap = cm.linear.YlOrRd_09.scale(min_density, max_density)
    colormap.caption = 'Population Density'

    # Crea una lista de umbrales manualmente
    threshold_scale = np.linspace(min_density, max_density, 6).tolist()  # Ajusta a 6 u otro número si deseas más intervalos

    # Crea un mapa base
    m = folium.Map(location=[20, 0], tiles='cartodbpositron', zoom_start=2, width=width, height=height)

    # Crea y añade el mapa coroplético al mapa base
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        data=df_2023,
        columns=['Code', 'Population density'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        threshold_scale=threshold_scale,  # Usa la lista de umbrales creada
        reset=True
    ).add_to(m)

    # Añade la escala de colores al mapa
    colormap.add_to(m)

    # Añade el control de capas al mapa
    folium.LayerControl().add_to(m)

    return m

