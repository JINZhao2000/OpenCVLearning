import cv2

from opt_images import cv_show

img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)
b, g ,r = cv2.split(img)
print(b.shape)

img = cv2.merge((b, g ,r))
print(img.shape)

# R
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
cv_show('Red', cur_img)

# B
cur_img = img.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0
cv_show('Blue', cur_img)

# G
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 2] = 0
cv_show('Green', cur_img)