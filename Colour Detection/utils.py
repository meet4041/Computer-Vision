import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = int(hsvC[0][0][0])

    # Use a wider range so real camera lighting still matches the target color.
    lowerLimit = np.array([max(hue - 20, 0), 50, 50], dtype=np.uint8)
    upperLimit = np.array([min(hue + 20, 179), 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
