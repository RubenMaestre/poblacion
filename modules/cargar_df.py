# cargar_df.py
import pandas as pd

def cargar_df():
    """Carga los DataFrames desde archivos Parquet y los devuelve."""
    try:
        df = pd.read_parquet('data/df.parquet')
        df_continentes = pd.read_parquet('data/df_continentes.parquet')
        df_ingresos= pd.read_parquet('data/df_ingresos.parquet')
        return df, df_continentes, df_ingresos
    except Exception as e:
        print(f"Error al cargar los DataFrames: {e}")
        return None, None, None
