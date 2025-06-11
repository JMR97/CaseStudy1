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

The dataset is saved as: cricket_matches_1000.csv   (Upload in the Github)


---

## 🧠 Overview
This project aims to build and evaluate a classification model. Key goals include:

Load and preprocess datasets

Split data for training and testing

Train a classifier (e.g., logistic regression, decision tree)

Evaluate performance using metrics and visual tools

Generate a confusion matrix for true vs predicted labels

Summarize findings in results.pdf

---

## 🛠️ Setup & Requirements
Install dependencies (example):

bash
Copy
Edit
pip install numpy pandas scikit-learn matplotlib seaborn
Feel free to use Conda or Pipenv as preferred.

---

## 🚦 How to Run
Preprocess data
python Codes/data_preprocessing.py --input DataSet/raw_data.csv --output DataSet/processed_data.csv

Train model
python Codes/train_model.py --data DataSet/processed_data.csv --model_output model.pkl

Evaluate
python Codes/evaluate.py --model model.pkl --data DataSet/processed_data.csv --report_dir reports/

Plot confusion matrix
python Codes/plot_confusion.py --y_true reports/y_true.npy --y_pred reports/y_pred.npy --output Confusion\ Matrix/confusion_matrix.png

---

## 🧪 Results
Check results.pdf for a comprehensive report, including:

Model performance metrics (accuracy, precision, recall, F1-score)

Confusion matrix plot

Observations and interpretation






