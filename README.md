#  Cricket Match Outcome Predictor

---

## 🧠 Overview
This project aims to build and evaluate a classification model. Key goals include:

Generate the datasets

Load and preprocess datasets

Split data for training and testing

Train a classifier (e.g., random forest, decision tree)

Evaluate performance using metrics and visual tools

Generate a confusion matrix for true vs predicted labels

Summarize findings in results.pdf

---



## 🏏 Introduction
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

The dataset is saved as: cricket_matches_1000.csv   (Upload in the Github)


---


## 🛠️ Setup & Requirements
Install dependencies (example):

`pip install numpy pandas scikit-learn matplotlib seaborn`

Feel free to use Conda or Pipenv as preferred.

---

## 🚦 How to Run

Select a folder where the Genereted Dataset will be saved. and then add the path in the `dataset generation.py` and run it.
Then make the Dataset I used. After that `classification.py` for running the models where Test-Train and plotting section is included.

---

## 🧪 Results
Check results.pdf for a comprehensive report, including:

Model performance metrics (accuracy, precision, recall, F1-score)

Confusion matrix plot

Observations and interpretation






