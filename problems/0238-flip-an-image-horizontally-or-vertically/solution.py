import numpy as np

def flip_image(image, direction):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: 2D or 3D list/array representing a grayscale or RGB image
        direction: string, either 'horizontal' or 'vertical'
    
    Returns:
        Flipped image as a nested list, or -1 if input is invalid
    """
    try:
        image = np.array(image)
        if direction == "horizontal":
            image = image[:, ::-1]
        elif direction == "vertical":
            image = image[::-1, :]
        else:
            return -1
        return image

    except:
        return -1