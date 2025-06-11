#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 21:23:24 2025

@author: jmr
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Increase number of matches to 1000
n_matches = 1000

# Sample player names pool
player_pool = [f'Player{i}' for i in range(1, 101)]  # 100 players

# Sample venues and conditions
venues = ['Eden Gardens', 'MCG', 'Lord’s', 'Wankhede', 'Newlands']
weather_options = ['Sunny', 'Cloudy', 'Rainy', 'Humid']
toss_decisions = ['Bat', 'Bowl']
outcomes = ['Team_A_Wins', 'Team_B_Wins', 'Draw']

data = []

for i in range(n_matches):
    match_id = f"M{i+1:04d}"
    date = pd.Timestamp('2020-01-01') + pd.to_timedelta(np.random.randint(0, 1825), unit='D')  # 5 years range
    time = f"{np.random.randint(12, 21)}:00"
    team_a = ', '.join(np.random.choice(player_pool, size=11, replace=False))
    team_b = ', '.join(np.random.choice(player_pool, size=11, replace=False))
    venue = np.random.choice(venues)
    weather = np.random.choice(weather_options)
    toss_winner = np.random.choice(['Team_A', 'Team_B'])
    toss_decision = np.random.choice(toss_decisions)
    outcome = np.random.choice(outcomes, p=[0.45, 0.45, 0.10])  # Slight bias toward winning

    data.append([
        match_id, date.date(), time, team_a, team_b,
        venue, weather, toss_winner, toss_decision, outcome
    ])

columns = ['Match_ID', 'Date', 'Time', 'Team_A', 'Team_B',
           'Venue', 'Weather', 'Toss_Winner', 'Toss_Decision', 'Outcome']

df_1000 = pd.DataFrame(data, columns=columns)

# Save the 1000+ match dataset
csv_path_1000 = "/Users/jmr/Desktop/Answer/cricket_matches_1000.csv"
df_1000.to_csv(csv_path_1000, index=False)

csv_path_1000
