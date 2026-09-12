---
title: Customer Churn Predictor
emoji: 📡
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: "3.35.2"
app_file: app.py
pinned: false
python_version: "3.10"
license: mit
short_description: Predict telecom customer churn using Random Forest + SMOTE
---

# 📡 Customer Churn Predictor

A machine-learning web app that predicts whether a telecom subscriber is likely to churn, built on the **IBM Telco Customer Churn** dataset.

## 🧠 Model Details

| Item | Detail |
|------|--------|
| Algorithm | Random Forest Classifier (100 estimators) |
| Class balancing | SMOTE (Synthetic Minority Oversampling) |
| Train / Test split | 80 / 20, stratified |
| Test Accuracy | ~78% |
| Dataset | IBM Telco Customer Churn · 7,032 rows · 20 features |

## 🗂️ Features Used

**Demographics:** Gender, Senior Citizen, Partner, Dependents, Tenure  
**Services:** Phone, Multiple Lines, Internet, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV & Movies  
**Billing:** Contract type, Paperless Billing, Payment Method, Monthly & Total Charges  

## 🔍 Key Churn Drivers Found in Data

1. **Month-to-month contracts** — customers without commitment churn most
2. **Fiber optic internet** — higher charges correlate with higher churn
3. **Electronic check payment** — linked to higher churn rates
4. **Short tenure** — new customers are most at risk
5. **Lack of online security / tech support** — service gaps drive churn

## 🚀 How to Run Locally

```bash
git clone https://huggingface.co/spaces/<YOUR_USERNAME>/customer-churn-predictor
cd customer-churn-predictor
pip install -r requirements.txt
python app.py
```

## 📦 Tech Stack

- **Gradio** — interactive UI
- **scikit-learn** — Random Forest
- **imbalanced-learn** — SMOTE
- **pandas / numpy** — data processing
- **IBM Telco dataset** — loaded directly from GitHub

## 📄 License

MIT

