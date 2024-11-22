import pandas as pd
import numpy as np

file_path = "stats.xlsx"
data = pd.read_excel(file_path)
Teams = data['Team']
Goals_Scored_Home = data['Goals(Home)']
Goals_Scored_Away = data['Goals(Away)']
Home_Attack = data['Average Goals(Home)']
Away_Attack = data['Average Goals(Away)']

Goals_Conceded_Home = data['Goals Conceded (Home)']
Goals_Conceded_Away = data['Goals Conceded (Away)']
Home_Defense = data['Average Goals Conceded (Home)']
Away_Defense = data['Average Goals Conceded (Away)']

def simulate_match(home_team, away_team, home_attack, away_attack, home_defense, away_defense):
    home_expected_goals = home_attack * away_defense
    away_expected_goals = away_attack * home_defense
    
    home_goals = np.random.poisson(home_expected_goals)
    away_goals = np.random.poisson(away_expected_goals)
    
    if(home_goals > away_goals):
        return 3, 0  # Home wins
    elif(home_goals < away_goals):
        return 0, 3  # Away wins
    else:
        return 1, 1  # Draw

home_team = Teams.iloc[0]
away_team = Teams.iloc[1]

# Get the corresponding statistics for each team
home_attack = Home_Attack.iloc[0]
away_attack = Away_Attack.iloc[1]
home_defense = Home_Defense.iloc[0]
away_defense = Away_Defense.iloc[1]

# Simulate the match
home_points, away_points = simulate_match(home_team, away_team, home_attack, away_attack, home_defense, away_defense)

# Print the results
print(f"{home_team} points: {home_points}, {away_team} points: {away_points}")
