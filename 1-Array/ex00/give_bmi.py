import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("bad arguments")

        height_np = np.array(height)
        weight_np = np.array(weight)

        BMI_np = weight_np / (height_np ** 2)

        return BMI_np.tolist()

    except ValueError as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi)
    return (bmi_array > limit).tolist()
