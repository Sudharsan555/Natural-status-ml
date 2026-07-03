# Natural Status ML Prediction System

An AI/ML-based prediction system designed to estimate whether an athlete’s physiological profile aligns with natural bodybuilding characteristics.

This project demonstrates the practical application of machine learning for classification, feature engineering, anomaly detection, and real-time inference using a lightweight Flask interface.

---

## 🚀 Project Overview

The Natural Status ML Prediction System analyzes athlete biomarker and body composition data to generate:

✔ Natural Probability Score  
✔ Final Status Classification (NATURAL / UNNATURAL).

The system simulates a professional evaluation pipeline inspired by analytical screening tools.

---

## 🧠 Machine Learning Pipeline

The project implements an end-to-end ML workflow:

• Synthetic data generation  
• Feature engineering  
• Data scaling / normalization  
• Classification model  
• Anomaly detection model  
• Real-time prediction

---

## ⚙️ Key Features

✅ Intelligent Feature Engineering  
Derived physiological metrics improve model accuracy

✅ Robust Scaling  
Ensures stable predictions across varying input ranges

✅ Classification Model  
Predicts probability of natural profile alignment

✅ Anomaly Detection  
Identifies statistically unusual physiological combinations

✅ Real-Time Prediction Interface  
User input → instant ML inference via Flask

---

## 🏗 Tech Stack

**Language:** Python  
**ML Libraries:** Scikit-learn, NumPy  
**Model Persistence:** Joblib  
**Interface:** Flask  
**Frontend:** HTML / CSS (Dark UI)

---

## 📁 Project Structure

```
natural-status-ml/
│
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── README.md
│
├── models/                    # Trained ML models
│   ├── classifier.pkl
│   ├── scaler.pkl
│   └── anomaly_detector.pkl
│
├── src/
│   ├── synthetic_generator.py # Dataset generation
│   ├── feature_engineering.py # Derived features
│   ├── train_model.py         # Model training
│   └── predict.py             # Prediction logic
│
└── templates/
    └── index.html             # Prediction UI
```

---

## 📊 Input Parameters

The model evaluates:

• Age (years)  
• Height (cm)  
• Weight (kg)  
• Body Fat (%)  
• Lean Mass (kg)  
• Testosterone (ng/dL)  
• LH (IU/L)  
• FSH (IU/L)  
• HDL (mg/dL)  
• Hemoglobin (g/dL)

---

## 🧪 Example Input Values

### ✅ Example – Likely NATURAL Profile

```
Age: 24
Height: 175
Weight: 78
Body Fat: 12
Lean Mass: 68
Testosterone: 650
LH: 5.2
FSH: 4.8
HDL: 55
Hemoglobin: 15.1
```

Expected Output:

```
Natural Probability: High
Final Status: NATURAL
```

---

### ⚠️ Example – Likely UNNATURAL Profile

```
Age: 29
Height: 180
Weight: 102
Body Fat: 6
Lean Mass: 96
Testosterone: 1800
LH: 0.4
FSH: 0.3
HDL: 22
Hemoglobin: 18.2
```

Expected Output:

```
Natural Probability: Low
Final Status: UNNATURAL
```

---

## ▶️ Running the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Train models (first time only)

```bash
python src/train_model.py
```

---

### 3️⃣ Start prediction interface

```bash
python app.py
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🎯 Sample Output

✔ Natural Probability (%)  
✔ Final Status Prediction

Example:

Natural Probability: 82.4%  
Final Status: NATURAL

---

## 📌 Purpose of Project

This project was developed to demonstrate:

• Applied machine learning concepts  
• Feature engineering strategy  
• Model evaluation logic  
• Real-time inference systems  
• UI-driven ML interaction

---

## ⚠️ Important Disclaimer

This system is a **simulation / academic ML project**.

It does **NOT** provide medical, diagnostic, or regulatory conclusions.  
Predictions are based on synthetic training data and statistical modeling.

---

## 👨‍💻 Author

Sudharsan V  
Machine Learning & Software Development Enthusiast

---

## ⭐ Highlights

✔ End-to-end ML pipeline  
✔ No CSV dependency at runtime  
✔ Real-time prediction system  
✔ Clean dark-themed UI  
✔ Demonstrates practical AI deployment
