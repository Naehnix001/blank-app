import streamlit as st
import pandas as pd

# Daten für NBA-Teams
nba_teams = [
    {"Team": "Golden State Warriors", "Siege": 53, "Logo": "https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg"},
    {"Team": "Los Angeles Lakers", "Siege": 50, "Logo": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg"},
    {"Team": "Milwaukee Bucks", "Siege": 55, "Logo": "https://upload.wikimedia.org/wikipedia/en/4/4a/Milwaukee_Bucks_logo.svg"},
    {"Team": "Boston Celtics", "Siege": 60, "Logo": "https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg"},
    {"Team": "Miami Heat", "Siege": 48, "Logo": "https://upload.wikimedia.org/wikipedia/en/f/fb/Miami_Heat_logo.svg"},
    {"Team": "Memphis Grizzlies", "Siege": 44, "Logo": "https://upload.wikimedia.org/wikipedia/en/f/f1/Memphis_Grizzlies.svg"},
]

# Daten für Fußball-Teams
soccer_teams = [
    {"Team": "FC Barcelona", "Punkte": 84, "Logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg"},
    {"Team": "Real Madrid", "Punkte": 82, "Logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"},
    {"Team": "Manchester City", "Punkte": 89, "Logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"},
    {"Team": "Bayern München", "Punkte": 80, "Logo": "https://upload.wikimedia.org/wikipedia/en/1/1f/FC_Bayern_München_logo_%282017%29.svg"},
    {"Team": "Paris Saint-Germain", "Punkte": 78, "Logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"},
    {"Team": "VfL Wolfsburg", "Punkte": 55, "Logo": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Logo-VfL-Wolfsburg.svg"},
    {"Team": "VfL Borussia Mönchengladbach", "Punkte":43, "Logo":"https://upload.wikimedia.org/wikipedia/commons/8/81/Borussia_Mönchengladbach_logo.svg" }
]

# Top 3 Spieler der Memphis Grizzlies basierend auf Punkten pro Spiel
grizzlies_players = [
    {"Spieler": "Ja Morant", "Position": "PG", "PPG": 22.7, "RPG": 4.2, "APG": 7.4},
    {"Spieler": "Jaren Jackson Jr.", "Position": "PF", "PPG": 22.4, "RPG": 5.7, "APG": 2.0},
    {"Spieler": "Desmond Bane", "Position": "SG", "PPG": 18.8, "RPG": 6.0, "APG": 5.4},
]

# Top 3 Spieler des VfL Wolfsburg basierend auf Toren
wolfsburg_players = [
    {"Spieler": "Mohamed Amoura", "Position": "FW", "Tore": 10, "Assists": 9},
    {"Spieler": "Jonas Wind", "Position": "FW", "Tore": 8, "Assists": 4},
    {"Spieler": "Tiago Tomás", "Position": "FW", "Tore": 6, "Assists": 3},
]

st.set_page_config(page_title="🏆 Sport App", layout="wide")
st.title("🏆 Die besten Teams im Sport")

sport_option = st.selectbox("Wähle deinen Lieblingssport:", ["Basketball (NBA)", "Fußball (International)"])

if sport_option == "Basketball (NBA)":
    st.subheader("🏀 Top NBA Teams")
    team_names = [team["Team"] for team in nba_teams]
    team_selection = st.selectbox("Wähle dein Lieblingsteam:", team_names)

    for team in nba_teams:
        if team["Team"] == team_selection:
            st.image(team["Logo"], width=150)
            st.markdown(f"**{team['Team']}**")
            st.caption(f"Siege: {team['Siege']}")

            if team["Team"] == "Memphis Grizzlies":
                st.markdown("**Top 3 Spieler:**")
                for player in grizzlies_players:
                    st.write(f"{player['Spieler']} ({player['Position']}): {player['PPG']} PPG, {player['RPG']} RPG, {player['APG']} APG")

else:
    st.subheader("⚽ Top Fußballteams")
    team_names = [team["Team"] for team in soccer_teams]
    team_selection = st.selectbox("Wähle dein Lieblingsteam:", team_names)

    for team in soccer_teams:
        if team["Team"] == team_selection:
            st.image(team["Logo"], width=150)
            st.markdown(f"**{team['Team']}**")
            st.caption(f"Punkte: {team['Punkte']}")

            if team["Team"] == "VfL Wolfsburg":
                st.markdown("**Top 3 Spieler:**")
                for player in wolfsburg_players:
                    st.write(f"{player['Spieler']} ({player['Position']}): {player['Tore']} Tore, {player['Assists']} Assists")