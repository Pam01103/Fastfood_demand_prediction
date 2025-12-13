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
def load_data():
    df=pd.read_csv("Balaji Fast Food Sales.csv")  
    return df

df = load_data()

# -----------------------------------------------------------
# PESTAÑAS PRINCIPALES
# -----------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📌 Contexto del Negocio",
    "🔍 Exploración de Datos",
    "🧠 Toma de Decisiones",
    "🔮 Predicción de Demanda"
])
# -----------------------------------------------------------
#  TAB 1: Contexto del Negocio
# -----------------------------------------------------------
with tab1:
    st.header("📌 Contexto del Negocio")
    st.markdown("""
    ### El problema
    Los restaurantes enfrentan variaciones en la demanda que dificultan la planeación de inventarios,
    lo que puede provocar faltantes o desperdicio de insumos.

    ### Objetivo del proyecto
    Apoyar la toma de decisiones mediante el análisis de datos históricos y la predicción de la demanda
    de cada ítem del menú.
    """)

    st.subheader("📊 Panorama general de ventas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de Ventas", "—")
    with col2:
        st.metric("Número de Ítems", "—")
    with col3:
        st.metric("Periodo Analizado", "—")

    st.divider()

    st.subheader("Composición de ventas")
    st.info("Aquí puedes mostrar una gráfica general: comida vs bebida")

    # st.plotly_chart(fig_resumen)


