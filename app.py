import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Football Transfer Value Predictor")

st.write("Predict a player's market value using machine learning.")

goals = st.number_input("Goals", min_value=0, value=10)
assists = st.number_input("Assists", min_value=0, value=5)
minutes_percentage = st.number_input(
    "Minutes Played (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)
age = st.number_input("Age", min_value=16, value=23)
position = st.selectbox(
    "Position",
    ["Centre-Back", "Left-Back", "Right-Back", "Defensive Midfield", "Central Midfield", "Attacking Midfielder", "Left Winger", "Right Winger", "Centre-Forward", "Left Midfield", "Right Midfield", "Second Striker"]
)

if st.button("Predict Value"):
    player = pd.DataFrame([{
        "goals": goals,
        "assists": assists,
        "minutes_percentage": minutes_percentage,
        "age": age,
        "position": position
    }])

    prediction = model.predict(player)[0]
    prediction = max(0, prediction) # Ensure prediction is not negative

    st.metric(
        "Predicted Market Value",
        f"€{prediction:.2f}M"
    )

