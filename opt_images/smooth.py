import cv2
import numpy as np

from opt_images import cv_show

img = cv2.imread('../resources/noise.png', cv2.IMREAD_COLOR)
blur = cv2.blur(img, (3, 3))
# cv_show('blur', blur)

box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# cv_show('box', box)

# out of bound
box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
# cv_show('box2', box2)

gaussian = cv2.GaussianBlur(img, (3, 3), 1)
# cv_show('gaussian', gaussian)

median = cv2.medianBlur(img, 3)
# cv_show('median', median)

res = np.hstack((blur, box, box2, gaussian, median))
cv_show('all', res)
