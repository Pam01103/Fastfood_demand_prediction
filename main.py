import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------------------------------------
st.set_page_config(
    page_title="Predicción de Demanda – Balaji Fast Food ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Predicción de Demanda para Inventarios")
st.caption("Proyecto desarrollado para Business Intelligence")

# -----------------------------------------------------------
# CARGA DE DATOS (placeholder)
# -----------------------------------------------------------
@st.cache_data
 url="Balaji Fast Food Sales.csv"
     all_sheets=pd.read_excel(url, sheet_name=None)   
     return all_sheets['Switchbacks']

df = load_data()

# -----------------------------------------------------------
# TABS / PESTAÑAS
# -----------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📌 Contexto del Negocio",
    "🔍 Exploración de Datos",
    "🧠 Toma de Decisiones",
    "🔮 Predicción de Demanda"
])

