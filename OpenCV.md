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

