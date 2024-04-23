# paginas/densidad.py
import streamlit as st
import plotly.graph_objects as go
from modules.cargar_df import cargar_df
from modules.graph.top_20_density import plot_top_20_density
from modules.graph.grafica_densidad_mundo import plot_population_density_map

def display():
    df, df_continentes, df_ingresos = cargar_df()
    # Imagen de cabecera (si decides volver a incluirla)
    # st.image('sources/cabecera.jpg', use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Densidad</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("En esta página vas a encontrar datos prácticamente en brutos sobre la densidad de población. Quiero mostarlos como una primera toma de contacto en lo que va a ser el proyecto.")

    plot_top_20_density(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    plot_population_density_map(df)
    