# paginas/densidad.py
import streamlit as st
import plotly.graph_objects as go
from modules.cargar_df import cargar_df
from modules.graph.grafica_inicio import plot_top_20_density

def display():
    df, df_continentes, df_ingresos = cargar_df()
    # Imagen de cabecera (si decides volver a incluirla)
    # st.image('sources/cabecera.jpg', use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Densidad</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    plot_top_20_density(df)
    