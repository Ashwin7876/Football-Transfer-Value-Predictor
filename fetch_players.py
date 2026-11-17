import requests
import pandas as pd
from datetime import date

API_KEY = "Your API Key"

headers = {
    "X-Auth-Token": API_KEY
}

url = "https://api.football-data.org/v4/competitions/PL/teams"

response = requests.get(url, headers=headers)
response.raise_for_status() #whether the rquest was succeded
data = response.json()

players = []

for team in data ["teams"]:#loops through every team returned by the api
    for player in team.get("squad", []): #loops through the players in each team's squad.
        birthday = player.get("dateOfBirth")
        age = None
        if birthday:
            born = date.fromisoformat(birthday[:10])
            today = date.today()
            age = today.year - born.year
            age -= (today.month, today.day) < (born.month, born.day)
        players.append({
            "id" :player["id"],
            "name": player["name"],
            "team": team["name"],
            "age": age,
            "position": player.get("position")
        })

df = pd.DataFrame(players)
df.to_csv("players.csv", index = False)

print(df.head())