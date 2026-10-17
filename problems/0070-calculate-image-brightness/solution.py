import numpy as np
def calculate_brightness(img):
	try:
		img = np.array(img)
	except:
		return -1
	if np.sum(img[img > 255]) > 0:
		return -1
	try:
		return np.sum(img)/(len(img)*len(img[0]))
	except:
		return -1
