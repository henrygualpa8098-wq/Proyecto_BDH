import streamlit as st
import pandas as pd


st.title("Evaluación de Política Pública")
st.subheader("Desempleo juvenil en Ecuador")


# Cargar datos
datos = pd.read_csv("../datos/datos.csv")


st.write("Base de datos utilizada:")
st.dataframe(datos)


st.subheader("Evolución del desempleo juvenil")

st.line_chart(
    datos.set_index("Año")["Desempleo_Juvenil"]
)


st.subheader("Indicadores laborales juveniles")


col1, col2, col3 = st.columns(3)


col1.metric(
    "Desempleo juvenil 2024",
    str(datos.iloc[-1]["Desempleo_Juvenil"]) + "%"
)


col2.metric(
    "Empleo adecuado juvenil",
    str(datos.iloc[-1]["Empleo_Adecuado_Juvenil"]) + "%"
)


col3.metric(
    "Informalidad juvenil",
    str(datos.iloc[-1]["Informalidad_Juvenil"]) + "%"
)


st.info(
"""
Fuente:
INEC - ENEMDU

Proyecto:
Evaluación de políticas públicas de empleo juvenil mediante arquitectura multiagéntica.
"""
)