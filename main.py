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
time_options = sorted(df['time_of_sale'].dropna().unique())
item_options = sorted(df['item_name'].unique())
if 'date' in df.columns:
    df['day_of_week_num'] = df['date'].dt.dayofweek
    day_map = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
    df['day_name_es'] = df['day_of_week_num'].map(day_map)
    orden_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    item_options = sorted(df['item_name'].unique())
else:
    # Fallback si no hay columna 'date'
    orden_dias = []
    item_options = []

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
    st.markdown("""
    *¿Qué nos dice esta gráfica?*
    
    > La **distribución** de las ventas de comida y bebidas es **casi idéntica**. 
    Ambos tipos de ítems tienen un *rango de pedidos y variabilidad muy similares*, 
    con las bebidas mostrando solo una mediana marginalmente mayor que la comida 
    rápida.
    """)

# -----------------------------------------------------------
#  TAB 2: Exploración de Datos
# -----------------------------------------------------------
with tab2:
    st.header("🔍 Exploración de Datos")
    st.subheader("*¿Cómo se comportan las ventas?*")
    
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
    > A nivel de ítems, observamos que Panipuri (Fastfood) y Sugarcane juice 
    (Beverages) son los productos que típicamente se venden en mayor cantidad 
    por pedido, ambos con medianas alrededor de 8.5 a 9 unidades. Vadapav y Cold 
    coffee registran las medianas más bajas (6-7 unidades). Aunque el jugo de 
    caña tiene la mayor variabilidad en su 50% central de ventas, en general, 
    todos los ítems comparten un rango de venta total muy similar, sugiriendo 
    que los tamaños de pedido mínimo y máximo son consistentes en todo el menú.
    """)
    # -----------------------------------------------------------
       
    df['date'] = pd.to_datetime(df['date'],errors='coerce' )
    df['week'] = df['date'].dt.to_period('W').dt.start_time
        
    ventas_semanales = (
        df.groupby(['week', 'item_name', 'item_type'])['quantity']
        .sum()
        .reset_index()
    )
    item_order = sorted(df['item_name'].unique())
    
    fig = px.line(
        ventas_semanales,
        x='week',
        y='quantity',
        color='item_type',          # equivale a hue
        facet_col='item_name',      # equivale a col
        facet_col_wrap=2,           # equivale a col_wrap
        category_orders={'item_name': item_order},
        markers=True,
        title='Tendencia de Ventas Semanales Separadas por Ítem'
    )
        
    #fig.update_layout(
       # height=600,
       # xaxis_title="Semana",
       # yaxis_title="Cantidad Vendida",
       # margin=dict(t=100)
   # )

    #fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="Cantidad Vendida")
    
    fig.update_layout(
        xaxis_title="Semana",  # última fila, columna izquierda
        xaxis4_title="Semana",   # última fila, columna derecha
        yaxis4_title="",
        yaxis6_title="",
        yaxis8_title="",
        margin=dict(t=100),
        height=750,
    )
            
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    > La gráfica muestra la evolución semanal de las ventas por ítem, lo que 
    permite identificar tendencias, posibles patrones de crecimiento o estacionalidad
    en el consumo de ciertos productos.
    """)
    # -----------------------------------------------------------
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    df['day_of_week_num'] = df['date'].dt.dayofweek
    
    ventas_por_dia = (
        df.groupby(['day_of_week_num', 'item_name'])['quantity']
        .sum()
        .reset_index()
    )
    
    # Mapeo a español
    day_map_es = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    
    ventas_por_dia['day_name_es'] = ventas_por_dia['day_of_week_num'].map(day_map_es)
    
    orden_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    fig = px.bar(
        ventas_por_dia,
        x='day_name_es',
        y='quantity',
        facet_col='item_name',       # equivale a col
        facet_col_wrap=3,            # equivale a col_wrap
        category_orders={
            'day_name_es': orden_dias
    },
        title='Demanda Total por Día de la Semana, Separada por Ítem'
    )

    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="Cantidad Vendida")
    
    fig.update_xaxes(tickangle=-45)
    
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    
    fig.update_layout(
        height=750,
        margin=dict(t=100),
        yaxis8_title="",
        yaxis9_title="",
        yaxis5_title="",
        yaxis6_title=""
        
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    > Esta visualización permite comparar cómo varía la demanda de cada ítem a 
    lo largo de los días de la semana, destacando diferencias claras entre 
    productos y días específicos.

    A partir de estas visualizaciones, se identifican patrones claros de variación en la demanda por producto y por día, lo cual justifica el uso de análisis interactivo y modelos predictivos.
    """)


    #st.divider()
    #col1, col2, col3 = st.columns(3)

    #with col1:
      #  st.metric("Mayor cantidad por pedido", "9")
    #with col2:
        #st.metric("Menor cantidad por pedido", "6")
    #with col3:
        #st.metric("Favorito del público", "¿?")



# -----------------------------------------------------------
#  TAB 3: Toma de Decisiones
# -----------------------------------------------------------
with tab3:
    st.header("🧠 Toma de Decisiones")
    st.subheader("*¿Qué hacer con base en el historial?*")
    ##Gráfica Barras
    if orden_dias:
        st.subheader("Demanda Semanal Promedio por Ítem")
        default_items = list(item_options)
        #Filtro multiple
        selected_items = st.multiselect(
            'Selecciona los Ítems para Analizar la Demanda Semanal :', 
            options=item_options,
            default=default_items, 
            key='item_multiselect_tab3' 
        )

        if selected_items:
            df_filtered = df[df['item_name'].isin(selected_items)].copy()
            
            if not df_filtered.empty:
                ventas_pivot = df_filtered.pivot_table(
                    index='day_name_es',
                    columns='item_name',
                    values='quantity',
                    aggfunc='mean' 
                ).reindex(orden_dias, fill_value=0).reset_index()

                # Grafico
                fig_stacked = px.bar(
                    ventas_pivot,
                    x='day_name_es',
                    y=selected_items, # Lista de ítems para apilar
                    title='Demanda Promedio Semanal por Ítem',
                    labels={'day_name_es': 'Día de la Semana', 'value': 'Cantidad Promedio Vendida', 'item_name': 'Ítem'}
                )
                
                fig_stacked.update_layout(
                    xaxis_tickangle=-45,
                    legend_title_text='Ítem'
                )

                st.plotly_chart(fig_stacked, use_container_width=True)
            else:
                 st.warning("No hay datos disponibles para los ítems seleccionados.")
        else:
            st.warning("Por favor, selecciona al menos un ítem para visualizar la demanda.")

    st.divider()
    
