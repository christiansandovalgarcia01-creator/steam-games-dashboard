import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --- Cargar dataset con ruta robusta ---
BASE = Path(__file__).parent
df = pd.read_csv(BASE / "dataset" / "steam_games.csv")

st.set_page_config(page_title="Mi Dashboard", layout="wide")
st.title("🎮 Dashboard de Steam Games")
st.subheader("👀 Vista previa")
st.dataframe(df.head())

# --- Juegos por desarrollador ---
st.subheader("🏭 Juegos por desarrollador")
games_by_dev = (
    df
    .groupby("developer", as_index=False)
    .agg(n_games=("appid", "nunique"))
    .sort_values("n_games", ascending=False)
)


# --- Gráfico opcional ---
st.dataframe(games_by_dev)

fig = px.bar(
    games_by_dev.head(20),
    x="developer", y="n_games",
    title="Top 20 desarrolladores por número de juegos"
)
st.plotly_chart(fig, use_container_width=True)

