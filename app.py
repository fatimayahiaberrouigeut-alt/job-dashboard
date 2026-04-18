import streamlit as st
import pandas as pd

st.title("📊 Job Market Dashboard")

# lire le fichier
df = pd.read_csv("emploitic (2).csv")

# afficher nombre total
st.metric("Total Jobs", len(df))

# afficher tableau
st.subheader("📄 Données")
st.dataframe(df)

# top titres (si colonne existe)
if "title" in df.columns:
    st.subheader("📈 Top Jobs")
    st.bar_chart(df["title"].value_counts().head(10))
