import numpy as np
import matplotlib.pyplot as plt


def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted_image = 255 - array
    display_image(array, "Original")
    print(array)
    display_image(inverted_image, "Invert")
    return inverted_image


def ft_red(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, 1:] = 0
    display_image(array_copy, "Red")
    return array_copy


def ft_green(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, [0, 2]] = 0
    display_image(array_copy, "Green")
    return array_copy


def ft_blue(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, :2] = 0
    display_image(array_copy, "Blue")
    return array_copy


def ft_grey(array: np.ndarray) -> np.ndarray:
    grey_image = np.mean(array, axis=2)
    grey_image = np.stack([grey_image] * 3, axis=2)
    grey_image = grey_image.astype(np.uint8)
    display_image(grey_image, "Grey")
    return grey_image
