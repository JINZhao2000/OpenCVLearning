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

### 1.6 数值计算

```python
res = cv2.add(imgRGB, imgRGB)
```

### 1.7 图像融合

```python
imgResized = cv2.resize(img2, (img1.shape[0], img1.shape[1]))
cv2.resize(img2, (0, 0), fx=2, fy=1)
```

### 1.8 图像阈值

```python
ret, dst = cv2.threshold(src, thresh, maxval, type)
```

- src：输入图，只能输入单通道图像，通常来说是灰度图
- dst：输出图
- thresh：阈值
- maxval：当像素值超过了阈值（或者小于阈值，根据 type 来决定），所赋予的值
- type：二值化操作的类型，包含以下 5 种类型
    - cv2.THRESH_BINARY：超过阈值部分取 maxval（最大值），否则取 0
    - cv2.THRESH_BINARY_INV：THRESH_BINARY 的反转
    - cv2.THRESH_TRUNC：大于阈值部分设为阈值，否则不变
    - cv2.THRESH_TOZERO：大于阈值部分不改变，否则设为 0
    - cv2.THRESH_TOZERO_INV：THRESH_TOZERO 的反转

### 1.9 图像平滑

```python
# 均值滤波
# 简单的平均卷积操作
blur = cv2.blur(img, (3, 3))
# 方框滤波
# 基本和均值一样，可以选择归一化，未归一化容易越界
box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# 高斯滤波
# 高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
gaussian = cv2.GaussianBlur(img, (5, 5), 1)
# 中值滤波
# 相当于用zhi'ji
median = cv2.medianBlur(img, 5)
```

### 1.10 形态学 - 腐蚀操作

```python
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
```

### 1.11 形态学 - 膨胀操作

```python
kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(img, kernel, iterations=1)
```

### 1.12 开运算与闭运算

```python
kernel = np.ones((5, 5), np.uint8)
# 开 先腐蚀再膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 闭 先膨胀再腐蚀
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

### 1.13 梯度运算

```python
# 梯度 = 膨胀 - 腐蚀 （减去）
kernel = np.ones((7, 7), np.uint8)
gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)
```

