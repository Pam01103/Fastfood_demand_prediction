import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------------------------------------
st.set_page_config(
    page_title="Predicción de Ventas – Balaji Fast Food ",
    page_icon="🥪",
    layout="wide"
)

st.title("📈 Predicción de Ventas para Balaji Fast Food")
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
    "📈 Predicción de Demanda"
])
# -----------------------------------------------------------
#  TAB 1: Contexto del Negocio
# -----------------------------------------------------------
with tab1:
    st.header("📌 Contexto del Negocio")
    st.markdown("""
    ### El problema
    En el sector de alimentos y bebidas, la gestión de inventario y la dotación de
    personal son retos críticos. Si se subestima la demanda, se pierden ventas; si se
    sobrestima, se incurre en desperdicio (costo) y en exceso de personal.

    ### Propuesta de negocio 
    Se propone desarrollar un ***Modelo Predictivo de Ventas*** utilizando técnicas de 
    Aprendizaje Automático basado en los datos históricos de 
    Balaji Fast Food. Esta herramienta permitirá pronosticar la demanda futura.
    - **Optimización de Costos**: Al predecir las ventas diarias o semanales, el negocio puede
    ajustar mejor los pedidos de ingredientes, minimizando el desperdicio de alimentos perecederos.
    - **Mejora Operacional**: Permite una planificación más eficiente del personal (horarios), 
    asegurando que haya suficientes empleados durante las horas pico y evitando costos 
    innecesarios en horas de baja actividad.
    - **Decisiones Estratégicas**: La identificación de los factores clave que impulsan las 
    ventas puede informar decisiones sobre marketing o expansión.
    """)
    
    st.divider()
    
    st.subheader("📊 Panorama general de Balaji Food")

    col_text, col_img = st.columns([2, 1])  
    
    with col_text:
        st.markdown("""
    ### Productos que ofrece Balaji Food
    
    - **Alimentos**
      - Aalopuri  
      - Vadapav  
      - Panipuri  
      - Frankie  
      - Sandwich  
    
    - **Bebidas**
      - Sugarcane Juice  
      - Cold Coffee  

    """)
    
    with col_img:
        st.image(
            "https://scontent.fmex2-1.fna.fbcdn.net/v/t39.30808-6/417734827_861614219306482_4082626460313921741_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=awVaNUByAOoQ7kNvwE9kmAo&_nc_oc=AdmDHDhIsGk0fDr_BjWHjZhVlFWXaTrVBNBwgoDRrhmUHeSQYEb8e3TU0UEem4AYVnE&_nc_zt=23&_nc_ht=scontent.fmex2-1.fna&_nc_gid=wQyrAxfTL9XpGjnjKvyPfw&oh=00_AfnGu417FjgiinV4hmke_Rt60dGC2bbge2MWD6P39L5KuA&oe=6942D792",
            use_container_width=True
        )

    st.divider()

    st.subheader("Composición de ventas general")
    fig = px.box(
        df,
        x='item_type',
        y='quantity',
        title='Comida vs Bebida'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.info("¿Qué quieren decir estos números?")

# -----------------------------------------------------------
#  TAB 2: Exploración de Datos
# -----------------------------------------------------------
with tab2:
    st.header("🔍 Exploración de Datos")
    st.subheader("*¿Cómo se comportan las ventas?*")
    
    st.markdown("""### Distribución de la Cantidad Vendida por Ítem """) 
    
    fig = px.box(
        df,
        x='item_name',
        y='quantity',
        color='item_type',  
        title='Distribución de la Cantidad Vendida por Ítem'
    )
    
    fig.update_layout(
        xaxis_title="Ítem",
        yaxis_title="Cantidad Vendida",
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    > Este box plot permite analizar la variabilidad en la cantidad vendida de cada 
    ítem del menú, identificando productos con comportamientos más estables y 
    aquellos con mayor dispersión o presencia de valores atípicos.
    """)
    
    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mayor cantidad por pedido", "9")
    with col2:
        st.metric("Menor cantidad por pedido", "6")
    with col3:
        st.metric("Favorito del público", "¿?")
