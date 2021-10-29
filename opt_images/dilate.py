import cv2
import numpy as np

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)
kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(img, kernel, iterations=1)
cv_show('dilate', dilate)
