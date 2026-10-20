import numpy as np

def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    try:
        img = np.array(img)
        dummy = len(img)
        if pad_width < 0:
            return -1
    except:
        return -1
    try:
        height,width = img.shape
        matrix = np.zeros((height+pad_width*2, width+pad_width*2))
        height2,width2 = matrix.shape
        matrix[pad_width:height2-pad_width, pad_width:width2-pad_width] = img
        return matrix
    except:
        return -1