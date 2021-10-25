# OpenCV

## 0. 环境准备

Python 3.6.8（用默认 pip3.6，不要升级）

http://npm.taobao.org/mirrors/python/3.6.8/

OpenCV

https://pypi.org/project/opencv-python/3.4.1.15/#files

https://pypi.org/project/opencv-contrib-python/3.4.1.15/#files

## 1. 图像基本操作

### 1.1 数据读取-图像

```python
cv2.IMREAD_COLOR # 彩色图像
cv2.IMREAD_GRAYSCALE # 灰度图像
```

```python
import cv2


def cv_show(name='unnamed', src='', waitTime=0):
    cv2.imshow(name, src)
    cv2.waitKey(waitTime)  # 0 表示任意键终止
    cv2.destroyAllWindows()
   
# img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_COLOR)  # 默认通道是 Blue Green Red
img = cv2.imread('../resources/maki_avatar.jpeg', cv2.IMREAD_GRAYSCALE)
# cv_show('maki', img)
print(img.shape)
# 保存
cv2.imwrite('../resources/maki.png', img)
```

### 1.2 读取数据-视频

```python
import cv2

vc = cv2.VideoCapture('../resources/test.mp4')

if vc.isOpened():
    opened, frame = vc.read()
else:
    opened = False
print(opened)

while opened:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像转换
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:  #  27 => 用 esc t
            break

vc.release()
cv2.destroyAllWindows()
```

### 1.3 截取部分图像数据

```python
cutted = img[50:700, 50:700]
```

### 1.4 颜色通道数据

```python
b, g ,r = cv2.split(img)
img = cv2.merge((b, g ,r))

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
```

### 1.5 边界填充

```python
# 复制法，复制最边缘的像素
replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
# 反射法，对感兴趣的图像中的像素两边进行复制
# fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)
# 反射法，以最边缘像素为轴，对称
# gfedcb|abcdefgh|gfedcba
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT_101)
# 外包装法
# cdefgh|abcdefgh|abc
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
# 常数法，常数值填充
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)
```



