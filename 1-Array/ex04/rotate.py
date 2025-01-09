from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Load an image, slice a region, rotate the sliced image, and display it.

    The image is loaded from the given path,
    sliced from rows 100 to 500 and columns 400 to 800.
    It is then rotated by transposing the pixel values
    (rows and columns are swapped).
    The rotated image is displayed using matplotlib in grayscale.

    Raises:
        BaseException: Any error during image loading,
        slicing, rotation, or display is caught and printed.
    """
    try:
        img = ft_load("../animal.jpeg")

        sliced_img = img[100:500, 400:800, :1].squeeze()

        rows, cols = sliced_img.shape
        rotated_img = np.zeros((cols, rows), dtype=sliced_img.dtype)

        for y in range(rows):
            for x in range(cols):
                rotated_img[x][y] = sliced_img[y][x]

        print("New shape after Rotation:", rotated_img.shape)
        print(rotated_img)

        plt.imshow(rotated_img, cmap='gray')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
