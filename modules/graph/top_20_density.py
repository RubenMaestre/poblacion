import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st

def plot_top_20_density(df):
    # Filtrar el DataFrame para el año 2024
    df_2024 = df[df['Year'] == 2024]
    
    # Ordenar por densidad de población de mayor a menor y tomar los primeros 20
    top_20_density = df_2024.nlargest(20, 'Population density')

    # Crear un gráfico de barras con Plotly Express
    fig = px.bar(
        top_20_density,
        x='Entity',  # Nombres de los países
        y='Population density',  # Densidad de población
        title='Top 20 Países por Densidad de Población en 2024',
        labels={'Entity': 'País', 'Population density': 'Densidad de Población (personas por km²)'},
        color='Population density',  # Color en función de la densidad
        height=900
    )

    # Ordenar las barras de mayor a menor
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

    st.plotly_chart(plot_top_20_density(df), use_container_width=True)
