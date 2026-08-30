# Diabetes Prediction Challenge — Kaggle Playground Series S5E12

##  Overview

This repository contains solution to the **Kaggle Playground Series Season 5 Episode 12 — Diabetes Prediction Challenge (2025)**.

The objective of the competition is to:

> **Predict the probability that a patient will be diagnosed with diabetes.**

Submissions are evaluated using the **Area Under the Receiver Operating Characteristic Curve (ROC-AUC)** between the predicted probabilities and the observed binary target.

The dataset is synthetically generated from a deep learning model trained on the Diabetes Health Indicators Dataset. Feature distributions closely resemble real-world data, while ensuring test labels remain private.

---

## Problem Statement

Given tabular health-related indicators for each patient, the task is to:

- Predict the probability of `diagnosed_diabetes` for each individual in the test set.
- Output probabilities (not binary labels).
- Optimize performance using **ROC-AUC**.

---

## Dataset Description

- **Train file:** `train.csv`
- **Test file:** `test.csv`
- **Target variable:** `diagnosed_diabetes`
- **Identifier column:** `id`
- **Number of features:** 53
- **Type:** Tabular dataset (mixed numeric and categorical features)

---

## Model Used

### LightGBM (Gradient Boosting Decision Trees)

The primary model used in this solution is **LightGBM**, a highly optimized gradient boosting framework designed for efficiency and performance on large-scale tabular datasets.

### Why LightGBM?

- Excellent performance on structured/tabular data
- Handles categorical features natively
- Fast training with histogram-based splitting
- Strong regularization support
- Well-suited for ROC-AUC optimization
- Robust against overfitting with early stopping

---

## Model Architecture Background

LightGBM is based on **Gradient Boosting Decision Trees (GBDT)**.

### Core Principles

1. **Boosting**
   - Sequentially builds trees.
   - Each new tree corrects the errors of previous trees.

2. **Gradient Optimization**
   - Minimizes a differentiable loss function.
   - For binary classification, the objective is logistic loss.

3. **Leaf-wise Tree Growth**
   - Unlike level-wise growth (e.g., XGBoost),
   - LightGBM grows trees leaf-wise, selecting the leaf with maximum loss reduction.
   - Leads to faster convergence and higher accuracy.

4. **Histogram-based Splitting**
   - Reduces memory usage.
   - Speeds up training significantly.

---

## Training Configuration

- **Cross-validation:** Stratified K-Fold (5 folds)
- **Evaluation Metric:** ROC-AUC
- **Early Stopping:** Enabled
- **Categorical Handling:** Native categorical encoding via `category` dtype
- **Missing Values:** Median imputation (numeric), dedicated category for categorical missing values

### Key Hyperparameters

n_estimators: 8000
learning_rate: 0.02
num_leaves: 128
max_depth: -1
min_child_samples: 50
subsample: 0.8
colsample_bytree: 0.8
objective: binary

### Model Structure


```text
kaggle-1-diabetes-prediction-challenge/
│
├── artifacts/
│   ├── models/
│   ├── plots/
│   ├── metrics.json
│   └── oof_predictions.csv
│
├── src/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   │
│   └── models/
│       └── train.py
│
├── submission.csv
└── README.md
```

### Key Insights

        LightGBM is highly effective for tabular medical datasets.
        Native categorical handling improves performance.
        Early stopping prevents overfitting.
        ROC-AUC is threshold-independent, making ranking quality critical.


### Results

      Cross-Validation (OOF) ROC-AUC: 69664
      Public Leaderboard Score: 0.69664
      Private Leaderboard Score: 0.69434

<img width="1495" height="195" alt="image" src="https://github.com/user-attachments/assets/ad42a068-d915-4bd3-a69f-a323eb7f1d4e" />


### Diagnostic Outputs Generated

      ROC Curve (OOF)
      Precision-Recall Curve
      Calibration Curve
      Confusion Matrix (F1-optimized threshold)
      Feature Importance (Gain-based)
      Learning Curve (Validation AUC over boosting rounds)

All outputs are saved in the artifacts/ directory.


### License

This project is released under the MIT License. The competition dataset is provided by Kaggle under: Attribution 4.0 International (CC BY 4.0)

### References

    Kaggle Playground Series S5E12: Diabetes Prediction Challenge (2025)
    LightGBM Documentation: https://lightgbm.readthedocs.io/
    ROC-AUC Theory: Fawcett, T. (2006). An introduction to ROC analysis.






