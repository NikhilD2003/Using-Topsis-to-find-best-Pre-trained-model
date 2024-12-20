# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JKOwXJQNHF1l9MRlp5TfJWcJeM3k2cgn
"""

# Install necessary libraries
!pip install numpy pandas topsispy transformers

# Import libraries
import numpy as np
import pandas as pd
from topsispy import topsis
from transformers import pipeline

# Define pre-trained models for text similarity
models = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "sentence-transformers/paraphrase-MiniLM-L3-v2",
    "sentence-transformers/msmarco-MiniLM-L12-v3"
]

# Define evaluation metrics for each model (example values)
evaluation_metrics = {
    "Model": models,
    "Accuracy": [0.88, 0.87, 0.89],  # Example accuracies
    "Speed (ms)": [100, 80, 120],    # Example speed in milliseconds
    "F1-score": [0.90, 0.85, 0.92], # Example F1-scores
    "Resource Usage (MB)": [300, 200, 350]  # Memory usage
}

# Create a DataFrame for evaluation metrics
df = pd.DataFrame(evaluation_metrics)

# Normalize "Speed" and "Resource Usage" because lower values are better
df["Speed (ms)"] = 1 / df["Speed (ms)"]
df["Resource Usage (MB)"] = 1 / df["Resource Usage (MB)"]

# Prepare data for TOPSIS
data = df.iloc[:, 1:].values
weights = [0.4, 0.2, 0.3, 0.1]  # Weights for each metric
impacts = [1, 1, 1, -1]  # +1 for benefit criteria, -1 for cost criteria

# Apply TOPSIS
topsis_scores, topsis_ranks = topsis(data, weights, impacts)

# Add TOPSIS scores and ranks to the DataFrame
df["TOPSIS Score"] = topsis_scores
df["Rank"] = topsis_ranks.astype(int)

# Sort by rank
df = df.sort_values(by="Rank")

# Display results
print("TOPSIS Results for Text Sentence Similarity Models:")
print(df)

# Save results
df.to_csv("topsis_results_text_similarity.csv", index=False)
from google.colab import files
files.download("topsis_results_text_similarity.csv")