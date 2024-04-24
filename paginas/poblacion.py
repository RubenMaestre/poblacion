# paginas/poblacion.py
import streamlit as st
from streamlit_folium import folium_static
import plotly.graph_objects as go
from modules.cargar_df_pob import cargar_df_pob


def display():
    df_paises_pob, df_continentes_pob, df_sociedad_pob, df_mundo_pob = cargar_df_pob()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Población mundial</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción a la densidad de población con un tamaño de texto mayor
    st.markdown("""
    <style>
        .big-font {
            font-size:24px;
            text-align: justify;
        }
    </style>
    <div class="big-font">
        <p>X</p>
        </div>
    <hr style="margin-top: 2rem;">
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Texto de análisis
    st.markdown("""
        <div style="text-align: justify;">
            X
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

