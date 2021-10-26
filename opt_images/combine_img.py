import cv2
import matplotlib.pyplot as plt

from opt_images import cv_show

img1 = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)
img2 = cv2.imread('../resources/maki2.jpg', cv2.IMREAD_COLOR)

imgResized = cv2.resize(img2, (img1.shape[0], img1.shape[1]))
res = cv2.addWeighted(img1, 0.4, imgResized, 0.6, 0)
cv_show('res', res)

cv_show('resize', cv2.resize(img2, (0, 0), fx=2, fy=1))
