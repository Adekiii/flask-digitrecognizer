import numpy as np 


def bounding_box(img):
    x, y = np.where(img)

    top_left = x.min(), y.min()
    bottom_right = x.max(), y.max()

    return img[top_left[0] - 25:bottom_right[0] + 25,
               top_left[1] - 50:bottom_right[1] + 50]