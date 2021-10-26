import cv2

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)

res = cv2.add(img, img)
cv_show('add', img+10)
cv_show('add', img+img)
cv_show('add', res)
