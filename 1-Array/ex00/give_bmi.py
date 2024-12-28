import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise AssertionError("bad arguments")

        for x in range(len(height)):
            if (
                type(height[x]) not in (int, float)
                or type(weight[x]) not in (int, float)
            ):
                raise AssertionError("bad arguments")

        height_np = np.array(height)
        weight_np = np.array(weight)

        BMI_np = weight_np / (height_np ** 2)
        return BMI_np.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi)
    return (bmi_array > limit).tolist()
