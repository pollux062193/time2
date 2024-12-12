import streamlit as st
import pandas as pd
from datetime import datetime

# Simulated database (in-memory storage for now)
data_entries = []

# Application title
st.title("Lottery Management System - Listero")

# Navigation menu
menu = ["Home", "Entradas", "Resumen"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Bienvenido, Listero")
    st.write("Usa el menú de la izquierda para navegar entre las opciones disponibles.")

elif choice == "Entradas":
    st.subheader("Registrar Entrada")

    entry_type = st.radio("Selecciona el tipo de entrada:", ["Fijo", "Corrido", "Parle"])

    if entry_type in ["Fijo", "Corrido"]:
        # Form for Fijo/Corrido
        number = st.number_input("Número (1-99):", min_value=1, max_value=99, step=1)
        amount = st.number_input("Monto:", min_value=0.01, step=0.01)

        if st.button("Registrar Entrada"):
            entry = {
                "Tipo": entry_type,
                "Número(s)": str(number),
                "Monto": amount,
                "Fecha/Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            data_entries.append(entry)
            st.success(f"Entrada de {entry_type} registrada correctamente.")

    elif entry_type == "Parle":
        # Form for Parle
        number1 = st.number_input("Número 1 (1-99):", min_value=1, max_value=99, step=1, key="number1")
        number2 = st.number_input("Número 2 (1-99):", min_value=1, max_value=99, step=1, key="number2")
        amount = st.number_input("Monto:", min_value=0.01, step=0.01, key="amount")

        if st.button("Registrar Entrada", key="parle"):
            entry = {
                "Tipo": entry_type,
                "Número(s)": f"{number1}, {number2}",
                "Monto": amount,
                "Fecha/Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            data_entries.append(entry)
            st.success("Entrada de Parle registrada correctamente.")

elif choice == "Resumen":
    st.subheader("Resumen de Entradas")

    if data_entries:
        df = pd.DataFrame(data_entries)
        st.table(df)
    else:
        st.write("No hay entradas registradas aún.")

