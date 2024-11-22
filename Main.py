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
Home_Defense = data['Average Goals Against(Home)']
Away_Defense = data['Average Goals Against(Away)']


