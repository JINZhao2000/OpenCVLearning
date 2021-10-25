import cv2

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)
cutted = img[50:700, 50:700]
cv_show('cutted', cutted)