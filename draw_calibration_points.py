import cv2
import numpy as np

# print(cv2.__version__)
# 3.3.0
points_to_calibrate = [(0.5, 0.5), (0.1, 0.1), (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]


for point in points_to_calibrate:
    img_file_name = 'img/image' + str(point[0]) + '_' + str(point[1]) + '.png'
    img = cv2.imread(img_file_name)
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    height = 1920
    width = 1080

    circleX = int(width*point[0])
    circleY = int(height*point[1])
    cv2.imshow('screen', img)
    cv2.waitKey(2500)
exit()