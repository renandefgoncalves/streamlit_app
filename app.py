import streamlit as st
import joblib
import pandas as pd

# Carrega modelo
model = joblib.load("modelo.pkl")

st.title("Previsão de Risco de Enchentes")

# Inputs
mes = st.slider("Mês do Ano", 1, 12, 6)
chuva = st.number_input("Precipitação (mm)", 0.0, 500.0, 50.0)

# Predição
if st.button("Verificar Risco"):
    dados = pd.DataFrame({"mes": [mes], "chuva": [chuva]})
    resultado = model.predict(dados)[0]
    if resultado == 1:
        st.error("⚠️ Alto risco de enchente!")
    else:
        st.success("✅ Sem risco de enchente.")
