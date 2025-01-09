from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path and convert it to an RGB numpy array.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Image as a 3D numpy array in RGB format.

    Raises:
        BaseException: Any error during image
        loading or conversion is caught and printed.
    """
    try:
        img = Image.open(path)

        img = img.convert("RGB")
        img_np = np.array(img)

        print(f"The shape of image is: {img_np.shape}")
        return img_np

    except BaseException as e:
        print(type(e).__name__, ":", e)
