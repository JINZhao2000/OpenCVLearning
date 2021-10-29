import cv2
import numpy as np

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_GRAYSCALE)
cv_show('original', img)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv_show('thresh', thresh)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1)
cv_show('erosion', erosion)
