import cv2
import numpy as np

# print(cv2.__version__)
# 3.3.0
cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

img = np.full((210, 425, 3), 128, dtype=np.uint8)

height = img.shape[0]
width = img.shape[1]
circleX = int(width/2)
circleY = int(height/2)

cv2.rectangle(img, (0, 0), (width, height), (255, 255, 255),thickness=-1)
cv2.circle(img, (circleX,circleY),2, (0,0,0),lineType=cv2.LINE_AA,thickness=-1)

cv2.imshow('screen', img)
cv2.waitKey(5000)

circleX = int(width/2)
circleY = int(height/3)

cv2.rectangle(img, (0, 0), (width, height), (255, 255, 255),thickness=-1)
cv2.circle(img, (circleX,circleY),2, (0,0,0),lineType=cv2.LINE_AA,thickness=-1)

cv2.imshow('screen', img)
cv2.waitKey(5000)
