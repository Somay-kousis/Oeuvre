# customerchurn

## Overview
A large-scale telecom churn prediction system focused on detecting behavioral signals that indicate when customers are preparing to silently leave a platform.

The project evolved beyond a normal ML classification task and became an exploration of:
- behavioral decay
- retention psychology
- silent disengagement
- asymmetric business risk
- predictive behavioral modeling

Dataset scale:
- 118,839 subscriber accounts

Best model performance:
- ROC-AUC: 0.9176

Live Demo:
- https://customer-churn-fmj75lr7s-somaykousis-6282s-projects.vercel.app

---

## Core Philosophy

The project was built around one central realization:

> customers usually leave emotionally before they leave technically.

The system attempts to identify:
- silent disengagement
- friction accumulation
- behavioral decay
- retention-risk patterns

before the actual churn event occurs.

Instead of treating churn as:
- a binary classification problem

the project approaches it more like:
- behavioral signal detection

---

## Problem Statement

Telecom churn prediction systems often rely on:
- simplistic assumptions
- isolated metrics
- surface-level business rules

This project explores whether:
- engineered behavioral signals
- service adoption patterns
- payment behavior
- tenure psychology
- ecosystem integration

can better predict churn risk.

---

## Technical Stack

### Machine Learning
- Python
- scikit-learn
- XGBoost
- CatBoost
- Logistic Regression
- Decision Trees

### Data Processing
- pandas
- NumPy

### Visualization
- Matplotlib

### Deployment
- Vercel

---

## Core Features

### End-to-End ML Pipeline
Built complete workflows for:
- preprocessing
- feature engineering
- model training
- evaluation
- threshold calibration
- business-cost analysis

---

### Behavioral Feature Engineering
Custom engineered signals included:
- onboarding vulnerability
- ecosystem integration
- billing friction
- tenure decay
- payment automation
- service dependency

---

### Multi-Model Benchmarking
Models tested:
- Logistic Regression
- Decision Trees
- XGBoost
- CatBoost

The system compared:
- ROC-AUC
- precision
- recall
- F1-score
- threshold calibration
- business impact

---

### Threshold Optimization
Instead of using the default classification threshold (`0.50`), the project calibrated thresholds using asymmetric business costs.

Business assumptions:
- False Positive cost: $15
- False Negative cost: $80

The optimized threshold (`0.30`) improved overall business savings significantly.

---

## Engineered Behavioral Signals

### NewCustomer
```python
tenure <= 3
```

Represents onboarding vulnerability and early-stage friction.

---

### LoyalCustomer
```python
tenure >= 50
```

Represents inertia-based customer loyalty.

---

### TotalServices
Aggregated ecosystem integration score based on active services.

The insight:
> users deeply integrated into the ecosystem churn less frequently.

---

### AutoPayment
Tracks whether customers use automatic billing systems.

Observation:
> manual payment creates recurring moments for spending reconsideration.

---

### FiberUser
Behavioral signal linked to competitor-targeted churn pressure.

---

## Model Evaluation

### Logistic Regression
ROC-AUC:
- 0.9090

Limitation:
- struggled with non-linear relationships

---

### Decision Tree
ROC-AUC:
- 0.9000

Limitation:
- unstable rule behavior
- brittle splitting logic

---

### XGBoost
ROC-AUC:
- 0.9176

Best-performing model.

Chosen because it:
- captured non-linear behavioral interaction
- generalized better
- handled engineered features effectively

---

## Best Model Configuration

```json
{
  "n_estimators": 560,
  "learning_rate": 0.216,
  "max_depth": 3,
  "subsample": 0.790,
  "colsample_bytree": 0.702,
  "gamma": 0.202,
  "min_child_weight": 2,
  "reg_alpha": 0.403,
  "reg_lambda": 2.687
}
```

---

## Key Insights

### Churn Is Usually Quiet
Most churners:
- never contact support
- never complain publicly
- simply disappear

---

### Behavioral Decay Starts Early
Usage and engagement degradation appeared:
- up to 90 days before churn

---

### Ecosystem Lock-In Matters
Users connected to:
- security systems
- backups
- multiple services

showed lower churn probability.

---

### Pricing Alone Is Not Enough
High pricing mattered, but:
- tenure decay
- friction accumulation
- disengagement patterns

were stronger predictors.

---

## UI & Presentation Philosophy

The project presentation intentionally avoided:
- generic dashboard aesthetics
- sterile ML interfaces
- corporate reporting visuals

Instead, the interface was designed like:
- a classified behavioral investigation archive
- a declassified intelligence report
- a forensic analysis system

This direction made the project feel:
- narrative-driven
- atmospheric
- memorable
- emotionally engaging

---

## Interesting Design Direction

The README and project storytelling frame churn as:
> silent emotional departure rather than numerical loss.

The system language intentionally uses:
- investigation metaphors
- classified report aesthetics
- behavioral language
- forensic analysis framing

Examples:
- “silent exit events”
- “behavioral decay”
- “subscriber attrition”
- “friction phase”

---

## Challenges Faced

### Imbalanced Risk Thinking
A major challenge was realizing:
- precision alone is misleading

The project required thinking in:
- asymmetric business cost
- operational impact
- retention economics

instead of purely academic metrics.

---

### Feature Engineering Complexity
Raw dataset columns initially produced weak predictive power.

Performance improved significantly after:
- behavioral aggregation
- engineered lifecycle signals
- ecosystem relationship modeling

---

## What The Project Taught

The project helped build understanding of:
- behavioral ML systems
- business-oriented model calibration
- threshold optimization
- feature engineering
- retention systems
- predictive analytics
- cost-sensitive classification

It also shifted perspective toward:
> ML systems as tools for understanding human behavior patterns.

---

## Current Status
Completed and deployed.

Potential future improvements:
- real-time churn monitoring
- temporal sequence modeling
- survival analysis
- explainable AI systems
- customer intervention recommendation engine

---

## Tags
machine-learning, churn-prediction, xgboost, predictive-modeling, feature-engineering, classification, behavioral-analysis, retention-systems, ml-pipeline, business-intelligence