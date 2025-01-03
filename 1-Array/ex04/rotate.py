from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        img = ft_load("../animal.jpeg")

        sliced_img = img[100:500, 400:800, :1].squeeze()

        rows, cols = sliced_img.shape
        rotated_img = np.zeros((cols, rows), dtype=sliced_img.dtype)

        for i in range(rows):
            for j in range(cols):
                rotated_img[cols - j - 1][i] = sliced_img[i][j]

        print("New shape after Rotation:", rotated_img.shape)
        print(rotated_img)

        plt.imshow(rotated_img, cmap='gray')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
