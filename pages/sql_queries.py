import streamlit as st
import sqlite3
from utils.db_connection import get_connection

def app():
    st.title("🗃 SQL Analytics")

    conn = get_connection()
    cursor = conn.cursor()

    st.subheader("Run Custom SQL Query")
    query = st.text_area("Enter SQL query", "SELECT * FROM players LIMIT 5;")
    if st.button("Run"):
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            cols = [description[0] for description in cursor.description]
            st.dataframe(rows, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")
    conn.close()

app()

