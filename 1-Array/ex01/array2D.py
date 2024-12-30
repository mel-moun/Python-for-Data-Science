import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        family_np = np.array(family)
        print("My shape is:", family_np.shape)

        family_sl = family_np[start:end]
        print("My new shape is:", family_sl.shape)
        return family_sl.tolist()

    except Exception as e:
        print(type(e).__name__, ":", e)
