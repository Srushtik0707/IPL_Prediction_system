import pandas as pd
import random

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

data = []

for i in range(10000):

    team1 = random.choice(teams)
    team2 = random.choice(teams)

    while team1 == team2:
        team2 = random.choice(teams)

    toss_winner = random.choice([team1, team2])

    total_score = random.randint(120, 250)

    wickets = random.randint(0, 10)

    overs = round(random.uniform(5, 20), 1)

    winner = random.choice([team1, team2])

    row = {
        "team1": team1,
        "team2": team2,
        "toss_winner": toss_winner,
        "venue": random.choice(venues),
        "pitch_type": random.choice(pitch_types),
        "weather": random.choice(weather_conditions),
        "total_score": total_score,
        "wickets": wickets,
        "overs": overs,
        "winner": winner
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("ipl_dataset.csv", index=False)

print("Dataset Generated Successfully")
print(df.head())