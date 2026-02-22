import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal de la aplicación
st.header('Dashboard de Análisis de Vehículos')

# Leer los datos (ruta relativa al mismo directorio que `app.py`)
car_data = pd.read_csv('vehicles_us.csv')


# CASILLA 1: Histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# CASILLA 2: Gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
