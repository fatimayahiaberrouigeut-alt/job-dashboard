
    st.write(df.columns)
    st.subheader("🧠 Insights")

if "title" in df.columns:
    top_job = df["title"].value_counts().idxmax()
    st.write(f"Le job le plus demandé est : **{top_job}**")
