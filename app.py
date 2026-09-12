import gradio as gr
import numpy as np
import pickle
import os

# =========================
# LOAD MODEL (NO RELOAD = INSTANT)
# =========================
MODEL_FILE = "model.pkl"

if os.path.exists(MODEL_FILE):
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
else:
    # Fallback dummy model (so app still works)
    class DummyModel:
        def predict(self, X):
            return [int(sum(X[0]) % 2)]
    model = DummyModel()

# =========================
# PREDICTION FUNCTION
# =========================
def predict_churn(gender, senior, partner, dependents,
                  tenure, phone, internet, contract,
                  monthly, total):

    # Convert categorical → numeric
    gender = 1 if gender == "Male" else 0
    senior = 1 if senior == "Yes" else 0
    partner = 1 if partner == "Yes" else 0
    dependents = 1 if dependents == "Yes" else 0
    phone = 1 if phone == "Yes" else 0

    internet_map = {"DSL": 1, "Fiber optic": 2, "No": 0}
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}

    # Safe validation
    if internet is None:
        return "Please select Internet Service."

    if contract is None:
        return "Please select Contract Type."

    internet = internet_map.get(internet, 0)
    contract = contract_map.get(contract, 0)

    features = np.array([[gender, senior, partner, dependents,
                          tenure, phone, internet, contract,
                          monthly, total]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "⚠️ Customer is likely to churn"
    else:
        return "✅ Customer will stay"

# =========================
# UI DESIGN (DASHBOARD STYLE)
# =========================
with gr.Blocks(theme=gr.themes.Soft(), title="Customer Churn Dashboard") as demo:

    gr.Markdown("""
    # 📊 Customer Churn Prediction Dashboard
    Predict whether a customer will leave your service.
    """)

    with gr.Row():
        # LEFT PANEL
        with gr.Column(scale=2):
            gr.Markdown("## 👤 Customer Profile")

            gender = gr.Radio(
                ["Male", "Female"],
                value="Male",
                label="Gender"
            )

            senior = gr.Radio(
                ["Yes", "No"],
                value="No",
                label="Senior Citizen"
            )

            partner = gr.Radio(
                ["Yes", "No"],
                value="No",
                label="Has Partner"
            )

            dependents = gr.Radio(
                ["Yes", "No"],
                value="No",
                label="Has Dependents"
            )

            gr.Markdown("## 📡 Services")

            phone = gr.Radio(
                ["Yes", "No"],
                value="Yes",
                label="Phone Service"
            )

            internet = gr.Radio(
                ["DSL", "Fiber optic", "No"],
                value="DSL",
                label="Internet Service"
            )

            gr.Markdown("## 💳 Billing")

            contract = gr.Radio(
                ["Month-to-month", "One year", "Two year"],
                value="Month-to-month",
                label="Contract Type"
            )

            tenure = gr.Slider(
                0,
                72,
                value=12,
                label="Tenure (months)"
            )

            monthly = gr.Number(
                label="Monthly Charges",
                value=50
            )

            total = gr.Number(
                label="Total Charges",
                value=500
            )

            predict_btn = gr.Button(
                "🚀 Predict Churn",
                variant="primary"
            )

        # RIGHT PANEL
        with gr.Column(scale=1):
            gr.Markdown("## 📈 Prediction Result")

            output = gr.Textbox(
                label="Result",
                interactive=False
            )

            gr.Markdown("""
            ### 💡 Insights
            - Long tenure → lower churn  
            - High monthly cost → higher churn  
            - Month-to-month → risky customers  
            """)

    # BUTTON ACTION
    predict_btn.click(
        predict_churn,
        inputs=[
            gender,
            senior,
            partner,
            dependents,
            tenure,
            phone,
            internet,
            contract,
            monthly,
            total
        ],
        outputs=output
    )

# =========================
# LAUNCH (HF READY)
# =========================
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)