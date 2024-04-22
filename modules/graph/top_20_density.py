# modules/graph/top_20_density.py
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def plot_top_20_density(df):
    # Asegurarse de que el DataFrame contenga los datos correctos
    if df.empty or 'Year' not in df.columns or 'Population density' not in df.columns:
        st.write("DataFrame no tiene los datos necesarios.")
        return  # Usar return para salir si no hay datos adecuados

    # Filtrar datos para el año 2024
    df_2024 = df[df['Year'] == 2024]

    # Ordenar por densidad de población de mayor a menor y tomar los primeros 20
    top_20_densidad = df_2024.sort_values(by='Population density', ascending=False).head(20)

    # Crear un gráfico de círculos con puntos
    fig = go.Figure()

    for index, row in top_20_densidad.iterrows():
        # Calcular el número de puntos en función de la densidad (normalizado)
        num_points = int((row['Population density'] / top_20_densidad['Population density'].max()) * 100)

        # Añadir un scatter para cada país
        fig.add_trace(go.Scatter(
            x=[index % 5] * num_points,
            y=[index // 5] * num_points,
            mode='markers',
            marker=dict(size=10),
            name=row['Entity']
        ))

    fig.update_layout(
        title='Visualización de la Densidad de Población en 2024',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        showlegend=True
    )

    # Mostrar la figura en Streamlit directamente
    st.plotly_chart(fig, use_container_width=True)
