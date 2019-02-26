#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tobii_research as tr
import numpy as np
import cv2
from win32api import GetSystemMetrics

global_gaze_pos = [0,0]

found_eyetrackers = tr.find_all_eyetrackers()
eyetracker = found_eyetrackers[0]

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)


def gaze_data_callback(gaze_data):
    global gaze_data_string

    right_gaze_data = gaze_data['right_gaze_point_on_display_area']
    left_gaze_data = gaze_data['left_gaze_point_on_display_area']

    has_nan_gaze_data = np.isnan(right_gaze_data)
    has_nan_gaze_data.extend(np.isnan(left_gaze_data))

    for gaze_data in has_nan_gaze_data:
        if(gaze_data):
            return

    x = (right_gaze[0] + left_gaze[0]) / 2.0 * SCREEN_WIDTH
    y = (right_gaze[1] + left_gaze[1]) / 2.0 * SCREEN_HEIGHT
    global_gaze_pos = [x, y]
    print(global_gaze_pos)


if __name__ == '__main__':
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA,
                            gaze_data_callback, as_dictionary=True)
    img = np.full((255,255,255), 128, dtype=np.uint8)
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        x = int(global_gaze_pos[0])
        y = int(global_gaze_pos[1])

        cv2.circle(img, (x, y), 15, (0,0,0), thickness=-1)
        cv2.imshow('screen',img)
        cv2.waitKey(0)