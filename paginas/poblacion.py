# paginas/poblacion.py
import streamlit as st
from streamlit_folium import folium_static
import plotly.graph_objects as go
from modules.cargar_df_pob import cargar_df_pob


def display():
    #df_paises_pob, df_continentes_pob, df_sociedad_pob, df_mundo_pob = cargar_df_pob()
    st.markdown("# Página de Población")
    st.write("Si ves este mensaje, la página está cargando correctamente.")

