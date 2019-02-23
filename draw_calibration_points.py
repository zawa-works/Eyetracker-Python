import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0

img = np.full((210, 425, 3), 128, dtype=np.uint8)

cv2.rectangle(img, (50, 10), (125, 60), (255, 0, 0))
cv2.rectangle(img, (50, 80), (125, 130), (0, 255, 0), thickness=-1)
cv2.rectangle(img, (50, 150), (125, 200), (0, 0, 255), thickness=-1)
cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0))

cv2.rectangle(img, (175, 10), (250, 60), (255, 255, 255), thickness=8, lineType=cv2.LINE_4)
cv2.line(img, (175, 10), (250, 60), (0, 0, 0), thickness=1, lineType=cv2.LINE_4)
cv2.rectangle(img, (175, 80), (250, 130), (255, 255, 255), thickness=8, lineType=cv2.LINE_8)
cv2.line(img, (175, 80), (250, 130), (0, 0, 0), thickness=1, lineType=cv2.LINE_8)
cv2.rectangle(img, (175, 150), (250, 200), (255, 255, 255), thickness=8, lineType=cv2.LINE_AA)
cv2.line(img, (175, 150), (250, 200), (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

cv2.rectangle(img, (600, 20), (750, 120), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
cv2.rectangle(img, (601, 160), (751, 260), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
cv2.rectangle(img, (602, 300), (752, 400), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)

cv2.imwrite('data/dst/opencv_draw_argument.png', img)