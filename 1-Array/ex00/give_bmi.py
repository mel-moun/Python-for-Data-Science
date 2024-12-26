from typing import Union

def give_bmi(height: list[Union[int, float]], weight: list[Union[int, float]]) -> list[Union[int, float]]:
    BMI = list()
    for i in range(len(height)):
        BMI.append(weight[i] / (height[i] ** 2))
    return BMI

def apply_limit(bmi: list[Union[int, float]], limit: int) -> list[bool]:
    boolean = list()
    for i in range(len(bmi)):
        boolean.append(bmi[i] > limit)
    return boolean
