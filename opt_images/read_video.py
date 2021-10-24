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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break

vc.release()
cv2.destroyAllWindows()
