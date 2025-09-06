import streamlit as st

# Page config
st.set_page_config(
    page_title="Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Cricbuzz LiveStats Dashboard")
st.sidebar.success("Select a page from the sidebar 👈")

st.write("""
Welcome to **Cricbuzz LiveStats** 🎉  
This app provides:
- 📡 Live Match Updates  
- 📊 Player & Team Statistics  
- 🗃 SQL Analytics Queries  
- ✍️ CRUD Operations for DB  
""")
