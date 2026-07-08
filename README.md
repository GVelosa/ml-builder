# ML Builder

A visual platform for creating, training, and analyzing Machine Learning models — no coding required.

## Overview

ML Builder transforms datasets into trained models through a simple, guided, step-by-step interface. It abstracts the technical complexity of Machine Learning, making the process accessible without sacrificing a professional look and feel.

**Target audience:**
- Machine Learning students
- Data Science beginners
- Non-programmers who want to experiment with ML
- Professionals who want to validate datasets without writing code

## Features

The platform is organized as a linear flow, where each step builds on the previous one.

### 1. Upload
Upload a CSV or Excel (`.xlsx`) file to get started. The platform will display:
- Dataset name, row and column count
- Data preview
- Column types
- Null value identification

### 2. Config
Configure how the model will be trained:
- Select the target column
- Choose the problem type: **Classification** or **Regression**
- Select and remove columns as needed

### 3. Preprocessing
The platform automatically prepares the data before training:
- Null value treatment
- Categorical variable encoding
- Normalization / scaling
- Train/test split

### 4. Model Parameters
Choose a model and configure its parameters:

| Problem Type | Available Models |
|---|---|
| Classification | Logistic Regression, Random Forest Classifier |
| Regression | Linear Regression, Random Forest Regressor |

Key parameters (e.g. number of trees, max depth, train/test ratio) are exposed in a simplified form.

### 5. Training
Start the training process and follow along with:
- Progress indicator
- Current status
- Simplified logs

### 6. Results
Visualize model performance through metrics and charts:
- **Classification:** Accuracy, Precision, Recall, F1 Score
- **Regression:** RMSE, MAE
- Feature importance (when available)

## Tech Stack

- **UI:** [Flet](https://flet.dev) (Python)

## Getting Started

```bash
# Install dependencies
uv sync

# Run the app
python main.py
```
