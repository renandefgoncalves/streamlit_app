import streamlit as st
import pandas as pd
import joblib

# CARREGAR MODELO
model = joblib.load("modelo.pkl")

# DICIONÁRIO DE MESES
meses = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4,
    "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8,
    "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
}

# TÍTULO
st.title("🌧️ Previsão de Risco de Enchente")

# INPUTS DO USUÁRIO
mes_nome = st.selectbox("Mês", list(meses.keys()))
mes = meses[mes_nome]

dias_chuva = st.number_input("Dias com chuva no mês", min_value=0, max_value=31, value=5)
temp_min = st.number_input("Temperatura mínima (°C)", value=20.0)
temp_max = st.number_input("Temperatura máxima (°C)", value=26.0)
total = st.number_input("Total acumulado de chuva (mm)", value=50.0)

# BOTÃO
if st.button("Gerar previsão"):
    # DADOS DE ENTRADA
    dados = pd.DataFrame({
        "Mes": [mes],
        "Maxima": [temp_max],
        "NumDiasDeChuva": [dias_chuva],
        "Total": [total]
    })

    # PROBABILIDADE
    prob = model.predict_proba(dados)[0][1]
    st.write(f"🔍 Probabilidade de risco de enchente: **{prob:.2%}**")

    # LIMIAR PERSONALIZADO
    limiar = 0.3
    if prob > limiar:
        st.error("🚨 Risco de enchente detectado!")
    else:
        st.success("✅ Sem risco de enchente previsto.")
