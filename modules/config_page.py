# modules/config_page.py
import streamlit as st

def set_global_page_config():
    st.set_page_config(
        page_title="Proyecto sobre densidad de población mundial",
        page_icon="🌍",
        layout="wide"
    )
