import os
import sys

# Ensure project root is in Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from src.predict import predict_natural_status

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        form_data = {
            "age": request.form["age"],
            "height": request.form["height"],
            "weight": request.form["weight"],
            "bodyfat": request.form["bodyfat"],
            "lean_mass": request.form["lean_mass"],
            "testosterone": request.form["testosterone"],
            "lh": request.form["lh"],
            "fsh": request.form["fsh"],
            "hdl": request.form["hdl"],
            "hemoglobin": request.form["hemoglobin"],
        }

        prediction, confidence = predict_natural_status(form_data)

        # 🔍 DEBUG (temporary – you can remove later)
        print("Prediction:", prediction)
        print("Confidence:", confidence)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
