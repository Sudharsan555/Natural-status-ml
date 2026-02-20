import numpy as np
import joblib
from src.feature_engineering import engineer_features

classifier = joblib.load("models/classifier.pkl")
scaler = joblib.load("models/scaler.pkl")
anomaly_detector = joblib.load("models/anomaly_detector.pkl")

# 🔹 REQUIRED FEATURE ORDER (VERY IMPORTANT)
FEATURE_ORDER = [
    "age",
    "height",
    "weight",
    "bodyfat",
    "lean_mass",
    "testosterone",
    "lh",
    "fsh",
    "hdl",
    "hemoglobin",
]

def predict_natural_status(form_data: dict):
    """
    form_data: dictionary from Flask request.form
    """

    # 🔹 Convert dict → ordered list → float
    input_values = [float(form_data[field]) for field in FEATURE_ORDER]

    # 🔹 Convert to 2D NumPy array
    X = np.array(input_values).reshape(1, -1)

    # 🔹 Feature engineering
    X_eng = engineer_features(X)

    # 🔹 Scale
    X_scaled = scaler.transform(X_eng)

    # 🔹 Predictions
    class_pred = classifier.predict(X_scaled)[0]
    class_prob = classifier.predict_proba(X_scaled)[0]
    anomaly = anomaly_detector.predict(X_scaled)[0]

    if class_pred == 1 and anomaly == 1:
        return "NATURAL", round(class_prob[1] * 100, 2)
    else:
        return "UNNATURAL", round(max(class_prob) * 100, 2)
