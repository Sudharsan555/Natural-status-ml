import numpy as np

def engineer_features(X: np.ndarray):
    """
    X shape: (n_samples, n_features)
    Feature order:
    [age, height_cm, weight, bodyfat, lean_mass, test, lh, fsh, hdl, hb]
    """

    height_m = X[:, 1] / 100
    bmi = X[:, 2] / (height_m ** 2)

    lean_mass_ratio = X[:, 4] / X[:, 2]
    hormone_balance = X[:, 6] + X[:, 7]

    engineered = np.column_stack([
        X,
        bmi,
        lean_mass_ratio,
        hormone_balance
    ])

    return engineered
