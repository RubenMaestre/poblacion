#modules/graph/grafica_inicio.py
import plotly.express as px
import streamlit as st
from modules.cargar_df import cargar_df

# Cargar datos
df, df_continentes, df_ingresos = cargar_df()

def grafica_simple(df_continentes):
    if not df_continentes.empty:
        # Crear la figura utilizando Plotly Express
        fig = px.line(
            df_continentes,
            x='Year',  # Usa la columna 'Year' directamente para el eje x
            y='Population density',
            color='Entity',
            title='Evolución de la densidad de población por zona geográfica',
            labels={'Population density': 'Densidad de población (personas por km²)', 'Year': 'Año', 'Entity': 'Zona geográfica'}
        )

        # Mostrar la figura en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No hay datos disponibles para mostrar.")