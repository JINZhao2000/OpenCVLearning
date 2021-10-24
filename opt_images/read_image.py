import cv2

# img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)  # 默认通道是 Blue Green Red
img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_GRAYSCALE)
# cv_show('maki', img)
print(img.shape)
# 保存
cv2.imwrite('../resources/maki.png', img)
