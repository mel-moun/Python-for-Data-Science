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
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    ft_display(red, "Red")
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    ft_display(green, "Green")
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    ft_display(blue, "Blue")
    return blue

def ft_grey(array: np.ndarray) -> np.ndarray:
    height = len(array)
    width = len(array[0])
    grey = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            grey[y][x] = array[y][x][1:2]

    ft_display(grey, "Grey")
    return grey
