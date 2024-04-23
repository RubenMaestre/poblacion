import folium
from streamlit_folium import folium_static

def plot_population_density_map(df):
    # Filtrar el DataFrame para el año 2024
    df_2024 = df[df['Year'] == 2024]

    # Inicializar un mapa del mundo con un tamaño específico
    m = folium.Map(location=[20, 0], tiles="cartodbpositron", zoom_start=2, width='1080px', height='720px')

    # Usar un Choropleth para visualizar la densidad de población
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        name='choropleth',
        data=df_2024,
        columns=['Code', 'Population density'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Densidad de población (personas por km²)',
        nan_fill_color='white'  # Color para países sin datos
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    folium_static(m)
