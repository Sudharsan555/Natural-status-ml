def validate_input(data):
    if len(data) != 10:
        raise ValueError("Input must contain exactly 10 values")

    for value in data:
        if value <= 0:
            raise ValueError("All input values must be positive")

    return True
