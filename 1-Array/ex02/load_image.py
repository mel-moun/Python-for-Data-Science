from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)

        img = img.convert("RGB")
        img_np = np.array(img)

        print(f"The shape of image is: {img_np.shape}")
        return img_np

    except BaseException as e:
        print(type(e).__name__, ":", e)
