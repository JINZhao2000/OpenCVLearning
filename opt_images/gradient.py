import cv2
import numpy as np

from opt_images import cv_show

pie = cv2.imread("../resources/pie.png")
kernel = np.ones((7, 7), np.uint8)
dilate = cv2.dilate(pie, kernel, iterations=5)
erosion = cv2.erode(pie, kernel, iterations=5)
gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)

res = np.hstack((dilate, erosion, gradient))
cv_show('res', res)


