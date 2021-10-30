import cv2
import numpy as np

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)
kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv_show('opening', opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv_show('closing', closing)

