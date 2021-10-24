import cv2


def cv_show(name='unnamed', src='', waitTime=0):
    cv2.imshow(name, src)
    cv2.waitKey(waitTime)  # 0 表示任意键终止
    cv2.destroyAllWindows()
