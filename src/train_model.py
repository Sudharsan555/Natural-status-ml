import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from data.synthetic_generator import generate_dataset
from src.feature_engineering import engineer_features
from src.anomaly_detection import train_anomaly_detector


def train_models():
    data = generate_dataset(1000)

    X = data[:, :-1]
    y = data[:, -1]

    X = engineer_features(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    classifier = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    classifier.fit(X_train, y_train)

    anomaly_model = train_anomaly_detector(X_train)

    joblib.dump(classifier, "models/classifier.pkl")
    joblib.dump(anomaly_model, "models/anomaly_detector.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    print("✅ Training completed successfully")
    print("📦 Models saved in /models folder")

if __name__ == "__main__":
    train_models()
