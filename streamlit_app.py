import streamlit as st
import pandas as pd

st.set_page_config(page_title="Screener LuxAlgo NASDAQ", layout="wide")

st.title("📊 Screener NASDAQ con LuxAlgo")

@st.cache_data
def carica_dati():
    url = "https://raw.githubusercontent.com/openai-sandbox/luxalgo-screener-data/main/nasdaq_luxalgo_screener.csv"
    return pd.read_csv(url)

df = carica_dati()

# Filtro volume medio 10 giorni > 100.000
df = df[df["avg_volume_10d"] > 100000]

# Visualizzazione tabella
st.dataframe(df, use_container_width=True)

# Esportazione
st.download_button("📥 Scarica dati filtrati", df.to_csv(index=False), file_name="luxalgo_screener.csv")
