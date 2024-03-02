# -*- coding: utf-8 -*-
"""disease prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17iiQApjHmzo0c6OlCcgTx_TB1XnILMv7
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

# Load training data from CSV files or any other suitable format
training_data = pd.read_csv('/content/symptoms to diseases.csv')  # Assuming training data is stored in a CSV file

# Extract symptoms and diseases from training data
symptoms = training_data['Symptoms'].tolist()
diseases = training_data['Diseases'].tolist()

# Convert symptoms to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(symptoms)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, diseases, test_size=0.2, random_state=42)

# Train Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Predict disease for new symptoms
new_symptoms = ["tired everyday and mild  fever and headache"]
new_symptoms_vectorized = vectorizer.transform(new_symptoms)
predicted_disease = classifier.predict(new_symptoms_vectorized)

print("Predicted disease:", predicted_disease[0])