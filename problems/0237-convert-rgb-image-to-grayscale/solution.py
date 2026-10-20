import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    result = []
    for h in range(len(image)):
        row = []
        for w in range(len(image[0])):
            try:
                r = image[h][w][0]
                g = image[h][w][1]
                b = image[h][w][2]
                if r > 255 or g > 255 or b > 255:
                    return -1
                gray = r * 0.299 + g * 0.587 + b * 0.114
                gray = round(gray)
                row.append(gray)
            except:
                return -1
        result.append(row)
    return result