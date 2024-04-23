# paginas/densidad.py
import streamlit as st
from streamlit_folium import folium_static
import plotly.graph_objects as go
from modules.cargar_df import cargar_df
from modules.graph.top_20_density import plot_top_20_density
from modules.graph.grafica_densidad_mundo import plot_population_density_map_with_plotly

def display():
    df, df_continentes, df_ingresos = cargar_df()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Densidad de Población</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Texto de análisis
    st.markdown("""
        <div style="text-align: justify;">
            <p>En nuestra exploración de datos globales, presentamos una visualización clave: el ranking de los 20 países con mayor densidad de población en el año 2024. Esta gráfica revela una tendencia fascinante: una significativa representación de microestados y territorios pequeños entre los más densamente poblados. Sobresalen entidades como Macao y Mónaco, junto con Singapur y Hong Kong, conocidos por sus extensas infraestructuras urbanas concentradas en áreas geográficas reducidas.</p>
            <p>La densidad de población, que mide la cantidad de personas por kilómetro cuadrado, varía ampliamente a nivel global y refleja no solo las dinámicas poblacionales sino también las políticas urbanísticas, el desarrollo económico y los factores geográficos. Los líderes de esta lista tienden a ser regiones altamente urbanizadas, donde la optimización del espacio ha sido primordial para acomodar a una población en crecimiento constante.</p>
            <p>Si bien la representación visual de estos datos es clara, es importante considerar la naturaleza de la gráfica. La inclusión sin filtros de todos los países, independientemente de su tamaño o población total, ofrece un panorama sin adulterar de la densidad de población. No obstante, cabe reflexionar sobre si este método ofrece la imagen más precisa de las condiciones de vida y de la presión sobre los recursos y servicios. Futuras investigaciones podrían incorporar umbrales como un mínimo de población o un área superficial específica, para refinar aún más nuestra comprensión de la densidad de población y sus implicaciones.</p>
            <p>Mientras tanto, esta gráfica sirve como un punto de partida interesante para discutir cómo y por qué ciertas regiones del mundo han evolucionado hacia concentraciones poblacionales tan altas. También es un recordatorio de las variadas experiencias de vida en el planeta, desde vastos paisajes con pocos habitantes hasta pequeños enclaves vibrantes y abarrotados de gente.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    plot_top_20_density(df)

    st.markdown("<br><br>", unsafe_allow_html=True)

    fig = plot_population_density_map_with_plotly(df)
    st.plotly_chart(fig, use_container_width=True)
