import numpy as np
def translate_object(points, tx, ty):
    translate_points = points
    translate_points = np.array(translate_points)
    translate_points[:, 0] +=tx
    translate_points[:,1] +=ty
    return translate_points
