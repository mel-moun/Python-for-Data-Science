import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    inverted = 255 - array
    print(array)
    ft_display(array, "Original")
    ft_display(inverted, "Invert")
    return inverted


def ft_display(array: np.ndarray, title: str):
    plt.imshow(array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_red(array: np.ndarray) -> np.ndarray:
    red = array.copy()
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i, j, 1] = 0
            red[i, j, 2] = 0
    ft_display(red, "Red")
    return red

