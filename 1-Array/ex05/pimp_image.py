import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, 1:] = 0
    return array_copy


def ft_green(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, [0, 2]] = 0
    return array_copy


def ft_blue(array: np.ndarray) -> np.ndarray:
    array_copy = array.copy()
    array_copy[:, :, :2] = 0
    return array_copy


def ft_grey(array: np.ndarray) -> np.ndarray:
    grey_image = np.mean(array, axis=2)
    grey_image = np.stack([grey_image] * 3, axis=2)
    return grey_image.astype(np.uint8)
