from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("ipl_model.pkl")

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

team_map = {team: i for i, team in enumerate(teams)}
venue_map = {venue: i for i, venue in enumerate(venues)}
pitch_map = {pitch: i for i, pitch in enumerate(pitch_types)}
weather_map = {weather: i for i, weather in enumerate(weather_conditions)}

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    if request.method == "POST":

        team1 = request.form["team1"]
        team2 = request.form["team2"]
        toss_winner = request.form["toss_winner"]
        venue = request.form["venue"]
        pitch_type = request.form["pitch_type"]
        weather = request.form["weather"]

        total_score = int(request.form["total_score"])
        wickets = int(request.form["wickets"])
        overs = float(request.form["overs"])

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

        result = model.predict(data)[0]

        reverse_team_map = {v: k for k, v in team_map.items()}

        prediction = reverse_team_map[result]

    return render_template(
        "index.html",
        prediction=prediction,
        teams=teams,
        venues=venues,
        pitch_types=pitch_types,
        weather_conditions=weather_conditions
    )

if __name__ == "__main__":
    app.run(debug=True)