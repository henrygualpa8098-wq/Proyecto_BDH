import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Proyecto BDH",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Evaluación del Impacto del Bono de Desarrollo Humano")
st.subheader("Proyecto Integrador Final")

# Leer la base de datos
df = pd.read_csv("datos/datos.csv")

st.divider()

# Gráfico de la pobreza
fig1 = px.line(
    df,
    x="Año",
    y="Pobreza",
    markers=True,
    title="Evolución de la pobreza en Ecuador"
)

st.plotly_chart(fig1, use_container_width=True)

# Gráfico de beneficiarios
fig2 = px.bar(
    df,
    x="Año",
    y="Beneficiarios",
    title="Beneficiarios del Bono de Desarrollo Humano"
)

st.plotly_chart(fig2, use_container_width=True)

# Gráfico de inversión
fig3 = px.area(
    df,
    x="Año",
    y="Inversion",
    title="Inversión pública en el Bono de Desarrollo Humano"
)

st.plotly_chart(fig3, use_container_width=True)