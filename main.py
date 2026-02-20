from src.predict import predict_natural_status

if __name__ == "__main__":
    sample_input = [
        25,     # Age
        175,    # Height (cm)
        78,     # Weight (kg)
        10,     # Body fat %
        70,     # Lean mass (kg)
        650,    # Testosterone (ng/dL)
        5.2,    # LH
        4.8,    # FSH
        58,     # HDL
        15.5    # Hemoglobin
    ]

    result = predict_natural_status(sample_input)

    print("\n🔬 Natural Status Prediction")
    print("----------------------------")
    for key, value in result.items():
        print(f"{key}: {value}")
