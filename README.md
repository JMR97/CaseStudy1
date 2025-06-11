# 🏏 Cricket Match Outcome Predictor

This machine learning project predicts the outcome of cricket matches based on match conditions and team combinations. It works with any mix of players regardless of nationality and uses multiple classifiers for robust evaluation.

---

## 🔍 Problem Statement

Develop a model that predicts the **match outcome** (Team A win, Team B win, or Draw) using:

- Match date and time
- Venue
- Weather conditions
- Toss winner and decision
- Team compositions (Team A and Team B)

---

## 📦 Dataset

We generated a **synthetic dataset** of 1000 matches, each including:

- `Team_A` and `Team_B` (each with 11 players randomly drawn from a player pool)
- `Venue`, `Weather`, `Toss_Winner`, `Toss_Decision`
- `Date`, `Time`
- `Outcome`: one of `Team_A_Wins`, `Team_B_Wins`, or `Draw`

The dataset is saved as:
