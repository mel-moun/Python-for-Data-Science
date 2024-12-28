from typing import Union

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert len(height) == len(weight), "bad arguments"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    BMI = list()
    for i in range(len(height)):
        BMI.append(weight[i] / (height[i] ** 2))
    return BMI

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    boolean = list()
    for i in range(len(bmi)):
        boolean.append(bmi[i] > limit)
    return boolean
