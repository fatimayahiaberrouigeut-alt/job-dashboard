import streamlit as st
import pandas as pd

st.title("📊 Job Market Dashboard")

df = pd.read_csv("emploitic (2).csv")

# 🔥 FILTRE PAR VILLE (si colonne existe)
if "location" in df.columns:
    villes = st.selectbox("Choisir une ville", ["Toutes"] + list(df["location"].dropna().unique()))
    
    if villes != "Toutes":
        df = df[df["location"] == villes]

st.metric("Total Jobs", len(df))

st.dataframe(df)
if "title" in df.columns:
    st.subheader("📈 Top Jobs")
    st.bar_chart(df["title"].value_counts().head(10))
    st.write(df.columns)
    st.subheader("🧠 Insights")

if "title" in df.columns:
    top_job = df["title"].value_counts().idxmax()
    st.write(f"Le job le plus demandé est : **{top_job}**")
