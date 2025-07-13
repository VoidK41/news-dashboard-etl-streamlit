import streamlit as st
import pandas as pd

st.set_page_config(page_title="Live news dashboard", layout="wide")

st.title("📰 Live News Dashboard")
st.caption("Powered by NewsAPI + Python")

df = pd.read_csv("output/news.csv")

# ===sidebar===
st.sidebar.header("🔍 Filter")
keyword = st.sidebar.text_input("search keyword (title):")
sources = df['source'].dropna().unique().tolist()
selected_source = st.sidebar.multiselect("Source", sources, default=sources)

# ===Filter===
if keyword:
    df = df[df['title'].str.contains(keyword, case=False, na=False)]
if selected_source:
    df = df[df['source'].isin(selected_source)]

st.markdown(f"### Showing {len(df)} articles")

for _, row in df.iterrows():
    st.markdown(f"**{row['title']}**")
    st.caption(f"🕒 {row['published_at']} | 📰 {row['source']}")
    st.markdown(f"[Read More]({row['url']})")
    st.markdown("---")