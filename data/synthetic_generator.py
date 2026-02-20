import random
import numpy as np

def generate_sample(natural=True):
    age = random.randint(18, 40)
    height = random.uniform(160, 190)  # cm

    if natural:
        weight = random.uniform(60, 90)
        body_fat = random.uniform(6, 18)
        testosterone = random.uniform(350, 900)
    else:
        weight = random.uniform(85, 120)
        body_fat = random.uniform(4, 12)
        testosterone = random.uniform(50, 2500)

    lean_mass = weight * (1 - body_fat / 100)
    lh = random.uniform(2, 8)
    fsh = random.uniform(2, 8)
    hdl = random.uniform(40, 70)
    hemoglobin = random.uniform(13, 17)

    label = 1 if natural else 0

    return [
        age,
        height,
        weight,
        body_fat,
        lean_mass,
        testosterone,
        lh,
        fsh,
        hdl,
        hemoglobin,
        label
    ]

def generate_dataset(samples=1000):
    data = []
    for _ in range(samples // 2):
        data.append(generate_sample(True))
        data.append(generate_sample(False))

    random.shuffle(data)
    return np.array(data)
