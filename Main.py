import pandas as pd
import numpy as np


file_path = "stats.xlsx"
data = pd.read_excel(file_path)

Teams = data['Team']
Home_Attack = data['Average Goals(Home)']
Home_Defense = data['Average Goals Conceded (Home)']
Away_Attack = data['Average Goals(Away)']
Away_Defense = data['Average Goals Conceded (Away)']
Home_Attack_Strength = data['Home Attack Strength']
Away_Attack_Stength = data['Away Attack Strength']
Home_Defense_Strength = data['Home Defense Strength']
Away_Defense_Strength = data['Away Defense Strength']
TotalPoints = data['Points']

team_points = {team: points for team, points in zip(Teams, TotalPoints)}

def simulate_match(home_team, away_team):
    homeIndex = Teams[Teams == home_team].index[0]
    awayIndex = Teams[Teams == away_team].index[0]
    
    home_attack = Home_Attack[homeIndex]
    home_defense = Home_Defense[homeIndex]
    away_attack = Away_Attack[awayIndex]
    away_defense = Away_Defense[awayIndex]

    home_attack_strength = Home_Attack_Strength[homeIndex]  # Avoid shadowing the global variable
    home_defense_strength = Home_Defense_Strength[homeIndex]
    away_attack_strength = Away_Attack_Stength[awayIndex]
    away_defense_strength = Away_Defense_Strength[awayIndex]

    home_expected_goals = home_attack_strength * away_defense_strength * home_attack * away_defense
    away_expected_goals = away_attack_strength * home_defense_strength * away_attack * home_defense
    
    home_goals = np.random.poisson(home_expected_goals)
    away_goals = np.random.poisson(away_expected_goals)

    home_points, away_points = determine_points(home_goals, away_goals)
    
    return home_goals, away_goals, home_points, away_points

def determine_points(home_goals, away_goals):
    if home_goals > away_goals:
        return (3, 0)  # Home win
    elif home_goals < away_goals:
        return (0, 3)  # Away win
    else:
        return (1, 1)  # Draw

    
fixtures = [
    ('Leicester City', 'Chelsea'),
    ('Bournemouth', 'Brighton'),
    ('Arsenal', 'Nottingham Forest'),
    ('Aston Villa', 'Crystal Palace'),
    ('Everton', 'Brentford'),
    ('Fulham', 'Wolverhampton Wanderers'),
    ('Manchester City', 'Tottenham Hotspur'),
    ('Southampton', 'Liverpool'),
    ('Ipswich Town', 'Manchester United'),
    ('Newcastle', 'West Ham United'),
    ('Brighton', 'Southampton'),
    ('Brentford', 'Leicester City'),
    ('Crystal Palace', 'Newcastle'),
    ('Nottingham Forest', 'Ipswich Town'),
    ('Wolverhampton Wanderers', 'Bournemouth'),
    ('West Ham United', 'Arsenal'),
    ('Chelsea', 'Aston Villa'),
    ('Manchester United', 'Everton'),
    ('Tottenham Hotspur', 'Fulham'),
    ('Liverpool', 'Manchester City'),
    ('Ipswich Town', 'Crystal Palace'),
    ('Leicester City', 'West Ham United'),
    ('Everton', 'Wolverhampton Wanderers'),
    ('Manchester City', 'Nottingham Forest'),
    ('Newcastle', 'Liverpool'),
    ('Southampton', 'Chelsea'),
    ('Arsenal', 'Manchester United'),
    ('Aston Villa', 'Brentford'),
    ('Fulham', 'Brighton'),
    ('Bournemouth', 'Tottenham Hotspur'),
    ('Everton', 'Liverpool'),
    ('Aston Villa', 'Southampton'),
    ('Brentford', 'Newcastle'),
    ('Crystal Palace', 'Manchester City'),
    ('Manchester United', 'Nottingham Forest'),
    ('Fulham', 'Arsenal'),
    ('Ipswich Town', 'Bournemouth'),
    ('Leicester City', 'Brighton'),
    ('Tottenham Hotspur', 'Chelsea'),
    ('West Ham United', 'Wolverhampton Wanderers'),
    ('Arsenal', 'Everton'),
    ('Liverpool', 'Fulham'),
    ('Newcastle', 'Leicester City'),
    ('Wolverhampton Wanderers', 'Ipswich Town'),
    ('Nottingham Forest', 'Aston Villa'),
    ('Brighton', 'Crystal Palace'),
    ('Manchester City', 'Manchester United'),
    ('Chelsea', 'Brentford'),
    ('Southampton', 'Tottenham Hotspur'),
    ('Bournemouth', 'West Ham United'),
    ('Aston Villa', 'Manchester City'),
    ('Brentford', 'Nottingham Forest'),
    ('Ipswich Town', 'Newcastle'),
    ('West Ham United', 'Brighton'),
    ('Crystal Palace', 'Arsenal'),
    ('Everton', 'Chelsea'),
    ('Fulham', 'Southampton'),
    ('Leicester City', 'Wolverhampton Wanderers'),
    ('Manchester United', 'Bournemouth'),
    ('Tottenham Hotspur', 'Liverpool'),
    ('Manchester City', 'Everton'),
    ('Bournemouth', 'Crystal Palace'),
    ('Chelsea', 'Fulham'),
    ('Newcastle', 'Aston Villa'),
    ('Nottingham Forest', 'Tottenham Hotspur'),
    ('Southampton', 'West Ham United'),
    ('Wolverhampton Wanderers', 'Manchester United'),
    ('Liverpool', 'Leicester City'),
    ('Brighton', 'Brentford'),
    ('Arsenal', 'Ipswich Town'),
    ('Leicester City', 'Manchester City'),
    ('Crystal Palace', 'Southampton'),
    ('Everton', 'Nottingham Forest'),
    ('Fulham', 'Bournemouth'),
    ('Tottenham Hotspur', 'Wolverhampton Wanderers'),
    ('West Ham United', 'Liverpool'),
    ('Aston Villa', 'Brighton'),
    ('Ipswich Town', 'Chelsea'),
    ('Manchester United', 'Newcastle'),
    ('Brentford', 'Arsenal'),
    ('Tottenham Hotspur', 'Newcastle'),
    ('Bournemouth', 'Everton'),
    ('Aston Villa', 'Leicester City'),
    ('Crystal Palace', 'Chelsea'),
    ('Manchester City', 'West Ham United'),
    ('Southampton', 'Brentford'),
    ('Brighton', 'Arsenal'),
    ('Fulham', 'Ipswich Town'),
    ('Liverpool', 'Manchester United'),
    ('Wolverhampton Wanderers', 'Nottingham Forest'),
    ('Brentford', 'Manchester City'),
    ('Chelsea', 'Bournemouth'),
    ('West Ham United', 'Fulham'),
    ('Nottingham Forest', 'Liverpool'),
    ('Everton', 'Aston Villa'),
    ('Leicester City', 'Crystal Palace'),
    ('Newcastle', 'Wolverhampton Wanderers'),
    ('Arsenal', 'Tottenham Hotspur'),
    ('Ipswich Town', 'Brighton'),
    ('Manchester United', 'Southampton'),
    ('Newcastle', 'Bournemouth'),
    ('Brentford', 'Liverpool'),
    ('Leicester City', 'Fulham'),
    ('West Ham United', 'Crystal Palace'),
    ('Arsenal', 'Aston Villa'),
    ('Everton', 'Tottenham Hotspur'),
    ('Manchester United', 'Brighton'),
    ('Nottingham Forest', 'Southampton'),
    ('Ipswich Town', 'Manchester City'),
    ('Chelsea', 'Wolverhampton Wanderers'),
    ('Bournemouth', 'Nottingham Forest'),
    ('Brighton', 'Everton'),
    ('Liverpool', 'Ipswich Town'),
    ('Southampton', 'Newcastle'),
    ('Wolverhampton Wanderers', 'Arsenal'),
    ('Manchester City', 'Chelsea'),
    ('Crystal Palace', 'Brentford'),
    ('Tottenham Hotspur', 'Leicester City'),
    ('Aston Villa', 'West Ham United'),
    ('Fulham', 'Manchester United'),
    ('Arsenal', 'Manchester City'),
    ('Bournemouth', 'Liverpool'),
    ('Brentford', 'Tottenham Hotspur'),
    ('Chelsea', 'West Ham United'),
    ('Everton', 'Leicester City'),
    ('Ipswich Town', 'Southampton'),
    ('Manchester United', 'Crystal Palace'),
    ('Newcastle', 'Fulham'),
    ('Nottingham Forest', 'Brighton'),
    ('Wolverhampton Wanderers', 'Aston Villa'),
    ('Aston Villa', 'Ipswich Town'),
    ('Brighton', 'Chelsea'),
    ('Crystal Palace', 'Everton'),
    ('Fulham', 'Nottingham Forest'),
    ('Leicester City', 'Arsenal'),
    ('Liverpool', 'Wolverhampton Wanderers'),
    ('Manchester City', 'Newcastle'),
    ('Southampton', 'Bournemouth'),
    ('Tottenham Hotspur', 'Manchester United'),
    ('West Ham United', 'Brentford'),
    ('Bournemouth', 'Wolverhampton Wanderers'),
    ('Arsenal', 'West Ham United'),
    ('Aston Villa', 'Chelsea'),
    ('Everton', 'Manchester United'),
    ('Fulham', 'Crystal Palace'),
    ('Ipswich Town', 'Tottenham Hotspur'),
    ('Leicester City', 'Brentford'),
    ('Manchester City', 'Liverpool'),
    ('Newcastle', 'Nottingham Forest'),
    ('Southampton', 'Brighton'),
    ('Brentford', 'Everton'),
    ('Brighton', 'Bournemouth'),
    ('Nottingham Forest', 'Arsenal'),
    ('Tottenham Hotspur', 'Manchester City'),
    ('West Ham United', 'Leicester City'),
    ('Wolverhampton Wanderers', 'Fulham'),
    ('Crystal Palace', 'Aston Villa'),
    ('Chelsea', 'Southampton'),
    ('Liverpool', 'Newcastle'),
    ('Manchester United', 'Ipswich Town'),
    ('Brentford', 'Aston Villa'),
    ('Brighton', 'Fulham'),
    ('Chelsea', 'Leicester City'),
    ('Crystal Palace', 'Ipswich Town'),
    ('Liverpool', 'Southampton'),
    ('Manchester United', 'Arsenal'),
    ('Nottingham Forest', 'Manchester City'),
    ('Tottenham Hotspur', 'Bournemouth'),
    ('West Ham United', 'Newcastle'),
    ('Wolverhampton Wanderers', 'Everton'),
    ('Bournemouth', 'Brentford'),
    ('Arsenal', 'Chelsea'),
    ('Aston Villa', 'Liverpool'),
    ('Everton', 'West Ham United'),
    ('Fulham', 'Tottenham Hotspur'),
    ('Ipswich Town', 'Nottingham Forest'),
    ('Leicester City', 'Manchester United'),
    ('Manchester City', 'Brighton'),
    ('Newcastle', 'Crystal Palace'),
    ('Southampton', 'Wolverhampton Wanderers'),
    ('Bournemouth', 'Ipswich Town'),
    ('Arsenal', 'Fulham'),
    ('Brighton', 'Aston Villa'),
    ('Nottingham Forest', 'Manchester United'),
    ('Wolverhampton Wanderers', 'West Ham United'),
    ('Chelsea', 'Tottenham Hotspur'),
    ('Manchester City', 'Leicester City'),
    ('Newcastle', 'Brentford'),
    ('Southampton', 'Crystal Palace'),
    ('Liverpool', 'Everton'),
    ('Aston Villa', 'Nottingham Forest'),
    ('Brentford', 'Chelsea'),
    ('Crystal Palace', 'Brighton'),
    ('Everton', 'Arsenal'),
    ('Fulham', 'Liverpool'),
    ('Ipswich Town', 'Wolverhampton Wanderers'),
    ('Leicester City', 'Newcastle'),
    ('Manchester United', 'Manchester City'),
    ('Tottenham Hotspur', 'Southampton'),
    ('West Ham United', 'Bournemouth'),
    ('Bournemouth', 'Fulham'),
    ('Arsenal', 'Brentford'),
    ('Brighton', 'Leicester City'),
    ('Chelsea', 'Ipswich Town'),
    ('Liverpool', 'West Ham United'),
    ('Manchester City', 'Crystal Palace'),
    ('Newcastle', 'Manchester United'),
    ('Nottingham Forest', 'Everton'),
    ('Southampton', 'Aston Villa'),
    ('Wolverhampton Wanderers', 'Tottenham Hotspur'),
    ('Aston Villa', 'Newcastle'),
    ('Brentford', 'Brighton'),
    ('Crystal Palace', 'Bournemouth'),
    ('Everton', 'Manchester City'),
    ('Fulham', 'Chelsea'),
    ('Ipswich Town', 'Arsenal'),
    ('Leicester City', 'Liverpool'),
    ('Manchester United', 'Wolverhampton Wanderers'),
    ('Tottenham Hotspur', 'Nottingham Forest'),
    ('West Ham United', 'Southampton'),
    ('Bournemouth', 'Manchester United'),
    ('Arsenal', 'Crystal Palace'),
    ('Brighton', 'West Ham United'),
    ('Chelsea', 'Everton'),
    ('Liverpool', 'Tottenham Hotspur'),
    ('Manchester City', 'Aston Villa'),
    ('Newcastle', 'Ipswich Town'),
    ('Nottingham Forest', 'Brentford'),
    ('Southampton', 'Fulham'),
    ('Wolverhampton Wanderers', 'Leicester City'),
    ('Arsenal', 'Bournemouth'),
    ('Aston Villa', 'Fulham'),
    ('Brentford', 'Manchester United'),
    ('Brighton', 'Newcastle'),
    ('Chelsea', 'Liverpool'),
    ('Crystal Palace', 'Nottingham Forest'),
    ('Everton', 'Ipswich Town'),
    ('Leicester City', 'Southampton'),
    ('Manchester City', 'Wolverhampton Wanderers'),
    ('West Ham United', 'Tottenham Hotspur'),
    ('Bournemouth', 'Chelsea'),
    ('Arsenal', 'Brighton'),
    ('Aston Villa', 'Leicester City'),
    ('Brentford', 'Fulham'),
    ('Crystal Palace', 'Manchester City'),
    ('Ipswich Town', 'West Ham United'),
    ('Liverpool', 'Newcastle'),
    ('Manchester United', 'Southampton'),
    ('Nottingham Forest', 'Everton'),
    ('Tottenham Hotspur', 'Wolverhampton Wanderers'),
    ('Bournemouth', 'Ipswich Town'),
    ('Arsenal', 'Wolverhampton Wanderers'),
    ('Brighton', 'Liverpool'),
    ('Chelsea', 'Crystal Palace'),
    ('Everton', 'Brentford'),
    ('Fulham', 'Southampton'),
    ('Leicester City', 'Manchester United'),
    ('Manchester City', 'Tottenham Hotspur'),
    ('Newcastle', 'Aston Villa'),
    ('West Ham United', 'Nottingham Forest'),
    ('Aston Villa', 'West Ham United'),
    ('Brentford', 'Arsenal'),
    ('Brighton', 'Manchester United'),
    ('Chelsea', 'Tottenham Hotspur'),
    ('Crystal Palace', 'Fulham'),
    ('Ipswich Town', 'Manchester City'),
    ('Liverpool', 'Nottingham Forest'),
    ('Southampton', 'Bournemouth'),
    ('Wolverhampton Wanderers', 'Leicester City'),
    ('Newcastle', 'Everton'),
]

# Function to run a single simulation of all remaining matches
def run_single_simulation():
    # Copy the initial points for each team
    simulated_points = team_points.copy()
    games_simulated = 0

    # Simulate all remaining matches and update the points
    for home_team, away_team in fixtures:
        home_goals, away_goals, home_points, away_points = simulate_match(home_team, away_team)

        if home_goals is not None and away_goals is not None:
            # Update the points for both teams
            simulated_points[home_team] += home_points
            simulated_points[away_team] += away_points
            games_simulated += 1

    return simulated_points

# Function to run Monte Carlo simulations
def monte_carlo_simulation(num_simulations=1000):
    simulation_results = []

    # Run the simulations
    for _ in range(num_simulations):
        simulated_points = run_single_simulation()
        simulation_results.append(simulated_points)

    # Convert the results into a DataFrame
    final_points = pd.DataFrame(simulation_results)

    # Calculate the average points over all simulations
    average_points = final_points.mean()

    # Sort teams based on the average points
    sorted_teams = average_points.sort_values(ascending=False)
    
    return sorted_teams

# Run the Monte Carlo simulation for 1000 simulations
final_predictions = monte_carlo_simulation(num_simulations=1000)

total_games_in_season = 38
games_already_played = 11
games_remaining = total_games_in_season - games_already_played

# Print the final predicted standings (average points)
print("Final Standings Prediction (Monte Carlo):")
for rank, (team, points) in enumerate(final_predictions.items(), start=1):
    currentPoints = team_points.get(team, 0)
    print(f"{rank}. {team} - {total_games_in_season} Games - {points + currentPoints:.2f} Points")


