import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# Load dataset
df = pd.read_csv("ipl_dataset.csv")

# Create label encoders
le_team1 = LabelEncoder()
le_team2 = LabelEncoder()
le_toss = LabelEncoder()
le_venue = LabelEncoder()
le_pitch = LabelEncoder()
le_weather = LabelEncoder()
le_winner = LabelEncoder()

# Convert text into numbers
df["team1"] = le_team1.fit_transform(df["team1"])
df["team2"] = le_team2.fit_transform(df["team2"])
df["toss_winner"] = le_toss.fit_transform(df["toss_winner"])
df["venue"] = le_venue.fit_transform(df["venue"])
df["pitch_type"] = le_pitch.fit_transform(df["pitch_type"])
df["weather"] = le_weather.fit_transform(df["weather"])
df["winner"] = le_winner.fit_transform(df["winner"])

# Input features
X = df.drop("winner", axis=1)

# Output feature
y = df["winner"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "ipl_model.pkl")

print("Model Saved Successfully")