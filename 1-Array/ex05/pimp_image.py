import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the input image array.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: Inverted image array.
    """
    try:
        inverted = 255 - array
        print(array)
        ft_display(array, "Original")
        ft_display(inverted, "Invert")
        return inverted
    except Exception as e:
        print(type(e).__name__, ":", e)


def ft_display(array: np.ndarray, title: str):
    """
    Display an image array with a given title using matplotlib.

    Args:
        array (np.ndarray): The image array to display.
        title (str): The title for the image.
    """
    try:
        plt.imshow(array)
        plt.title(title)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(type(e).__name__, ":", e)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extract the red channel from the image array and set other channels to 0.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The image with only the red channel.
    """
    try:
        red = array.copy()
        red[:, :, 1] = 0
        red[:, :, 2] = 0
        ft_display(red, "Red")
        return red
    except Exception as e:
        print(type(e).__name__, ":", e)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extract the green channel from the image array and set other channels to 0.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The image with only the green channel.
    """
    try:
        green = array.copy()
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        ft_display(green, "Green")
        return green
    except Exception as e:
        print(type(e).__name__, ":", e)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extract the blue channel from the image array and set other channels to 0.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The image with only the blue channel.
    """
    try:
        blue = array.copy()
        blue[:, :, 0] = 0
        blue[:, :, 1] = 0
        ft_display(blue, "Blue")
        return blue
    except Exception as e:
        print(type(e).__name__, ":", e)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the image array to a greyscale
    image by extracting the green channel.

    Args:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The greyscale image array.
    """
    try:
        height = len(array)
        width = len(array[0])
        grey = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                grey[y][x] = array[y][x][1:2]

        ft_display(grey, "Grey")
        return grey
    except Exception as e:
        print(type(e).__name__, ":", e)
