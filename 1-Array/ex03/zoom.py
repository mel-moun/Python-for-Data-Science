from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    try:
        img = ft_load("../animal.jpeg")
        print(img)

        sliced_img = img[100:500, 400:800, :1]

        print("New shape after slicing:", sliced_img.shape)
        print(sliced_img)

        plt.imshow(sliced_img.squeeze(), cmap='gray')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
