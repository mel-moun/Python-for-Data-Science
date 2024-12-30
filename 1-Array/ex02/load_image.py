from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        print(img_array)
        return img_array

    except BaseException as e:
        print(type(e).__name__, ":", e)
      