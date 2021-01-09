import numpy as np 


def bounding_box(img):
    x, y = np.where(img)

    top_left = x.min(), y.min()
    bottom_right = x.max(), y.max()

    return img[top_left[0] - 15:bottom_right[0] + 15,
               top_left[1] - 40:bottom_right[1] + 40]