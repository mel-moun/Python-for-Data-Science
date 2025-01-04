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
