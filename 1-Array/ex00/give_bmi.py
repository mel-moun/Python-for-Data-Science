import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI for each person given height and weight.

    Args:
        height (list): List of heights (in meters).
        weight (list): List of weights (in kilograms).

    Returns:
        list: List of BMI values.

    Raises:
        AssertionError: If height and weight lists have different lengths
        or contain invalid data types.
    """
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
    """
    Apply a limit to the BMI values and return if each value exceeds the limit.

    Args:
        bmi (list): List of BMI values.
        limit (int): The BMI limit to check against.

    Returns:
        list: List of boolean values indicating if BMI exceeds the limit.
    """
    bmi_array = np.array(bmi)
    return (bmi_array > limit).tolist()
