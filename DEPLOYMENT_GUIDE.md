# 🚀 Deploying to Hugging Face Spaces — Step-by-Step Guide

## Files in This Project

```
churn_app/
├── app.py            ← Main Gradio application (model + UI)
├── requirements.txt  ← Python dependencies
└── README.md         ← Space card (shown on HuggingFace)
```

---

## Step 1 — Create a Hugging Face Account

Go to https://huggingface.co and sign up (free).

---

## Step 2 — Create a New Space

1. Click your profile picture → **New Space**
2. Fill in:
   - **Space name:** `customer-churn-predictor` (or any name you like)
   - **License:** MIT
   - **SDK:** Gradio
   - **SDK Version:** 4.44.0
   - **Visibility:** Public *(or Private if preferred)*
3. Click **Create Space**

---

## Step 3 — Upload Your Files

### Option A — Via the Web UI (easiest)

1. Inside your Space, click **Files** → **Add file** → **Upload files**
2. Upload all three files:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Click **Commit changes to main**

### Option B — Via Git (recommended for updates)

```bash
# Install git-lfs first (only needed once)
git lfs install

# Clone your empty Space repo
git clone https://huggingface.co/spaces/YOUR_USERNAME/customer-churn-predictor
cd customer-churn-predictor

# Copy the project files into the cloned folder
cp /path/to/churn_app/app.py .
cp /path/to/churn_app/requirements.txt .
cp /path/to/churn_app/README.md .

# Push
git add .
git commit -m "Initial deployment"
git push
```

Replace `YOUR_USERNAME` with your actual HuggingFace username.

---

## Step 4 — Wait for Build

After pushing, HuggingFace will:
1. Install dependencies from `requirements.txt` (~60–90 sec)
2. Run `app.py`
3. Show **Running** status when ready

You can watch the build log in the **Logs** tab of your Space.

---

## Step 5 — Share Your App

Your app will be live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/customer-churn-predictor
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Build fails with `ModuleNotFoundError` | Check `requirements.txt` has all packages |
| `imbalanced-learn` not found | Make sure it's spelled exactly `imbalanced-learn` (not `imblearn`) |
| App crashes on launch | Check the **Logs** tab; usually a version mismatch |
| Dataset fails to load | The app fetches CSV from GitHub — ensure the Space has internet access (it does by default) |
| Gradio version conflict | Pin to `gradio==4.44.0` in requirements.txt |

---

## Upgrading the Model Later

To swap in a better model (e.g., XGBoost with tuned hyperparameters):
1. Edit `app.py` — replace the `RandomForestClassifier` block
2. Add `xgboost` to `requirements.txt`
3. Push the changes — Space rebuilds automatically

---

## Optional Enhancements

- **Add SHAP explanations** — show which features drove each prediction
- **Batch CSV upload** — let users upload a CSV and get predictions for all rows
- **Model card** — document fairness metrics and limitations in README.md
- **Persistent model file** — save `model.pkl` to avoid retraining on every cold start
