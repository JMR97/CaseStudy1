
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 13:22:22 2025
@author: jmr
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
path = "/Users/jmr/Desktop/Answer/cricket_matches_1000.csv"
df = pd.read_csv(path)


# Encode categorical columns

label_encoders = {}
categorical_columns = ['Venue', 'Weather', 'Toss_Winner', 'Toss_Decision', 'Outcome']

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


# Feature Engineering: Encode teams

df['Team_A_Hash'] = df['Team_A'].apply(lambda x: sum([hash(p) for p in x.split(', ')]) % 10000)
df['Team_B_Hash'] = df['Team_B'].apply(lambda x: sum([hash(p) for p in x.split(', ')]) % 10000)


# Prepare features and labels

X = df.drop(columns=['Match_ID', 'Date', 'Time', 'Team_A', 'Team_B', 'Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define models

models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
}


# Train, Predict, and Evaluate

for name, model in models.items():
    print(f"\n📌 Model: {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print("🎯 Accuracy: {:.2f}%".format(acc * 100))
    print("📊 Classification Report:\n", classification_report(y_test, y_pred))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    class_names = label_encoders['Outcome'].classes_
    
    print(class_names)

    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.title(f"{name} - Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()
