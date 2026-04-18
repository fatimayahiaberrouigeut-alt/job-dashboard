import streamlit as st
import pandas as pd

df = pd.read_csv("emploitic (2).csv")  # ⚠️ IMPORTANT

st.write(df.columns)
