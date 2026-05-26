import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("ipl_model.pkl")

st.set_page_config(
    page_title="IPL Prediction System",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 IPL Match Prediction System")

teams = [
    "CSK", "MI", "RCB", "KKR",
    "SRH", "RR", "DC", "PBKS",
    "GT", "LSG"
]

venues = [
    "Wankhede Stadium",
    "Chinnaswamy Stadium",
    "Eden Gardens",
    "Chepauk",
    "Narendra Modi Stadium"
]

pitch_types = ["Batting", "Bowling", "Balanced"]

weather_conditions = ["Hot", "Cloudy", "Humid"]

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)

toss_winner = st.selectbox("Select Toss Winner", teams)

venue = st.selectbox("Select Venue", venues)

pitch_type = st.selectbox("Pitch Type", pitch_types)

weather = st.selectbox("Weather", weather_conditions)

total_score = st.number_input("Total Score", 100, 300)

wickets = st.number_input("Wickets", 0, 10)

overs = st.number_input("Overs", 1.0, 20.0)

if st.button("Predict Winner"):

    if team1 == team2:
        st.error("Team 1 and Team 2 cannot be same")

    else:

        team_map = {team: i for i, team in enumerate(teams)}
        venue_map = {venue: i for i, venue in enumerate(venues)}
        pitch_map = {pitch: i for i, pitch in enumerate(pitch_types)}
        weather_map = {weather: i for i, weather in enumerate(weather_conditions)}

        data = pd.DataFrame([{
            "team1": team_map[team1],
            "team2": team_map[team2],
            "toss_winner": team_map[toss_winner],
            "venue": venue_map[venue],
            "pitch_type": pitch_map[pitch_type],
            "weather": weather_map[weather],
            "total_score": total_score,
            "wickets": wickets,
            "overs": overs
        }])

        prediction = model.predict(data)[0]

        reverse_team_map = {v: k for k, v in team_map.items()}

        st.success(f"Predicted Winner: {reverse_team_map[prediction]}")