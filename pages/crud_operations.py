import streamlit as st
from utils.db_connection import get_connection

def app():
    st.title("✍️ CRUD Operations")

    st.subheader("Add a New Player")
    name = st.text_input("Player Name")
    team_id = st.number_input("Team ID", min_value=1, step=1)
    runs = st.number_input("Runs", min_value=0, step=1)
    wickets = st.number_input("Wickets", min_value=0, step=1)

    if st.button("Add Player"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO players (player_name, team_id, runs, wickets) VALUES (?, ?, ?, ?)",
                       (name, team_id, runs, wickets))
        conn.commit()
        conn.close()
        st.success("✅ Player added successfully!")

