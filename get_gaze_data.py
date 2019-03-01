#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tobii_research as tr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from win32api import GetSystemMetrics

found_eyetrackers = tr.find_all_eyetrackers()  # アイトラッカーを見つける
my_eyetracker = found_eyetrackers[0]  # その中から0番目のアイトラッカーに接続する

# PCのスクリーンの解像度を取得
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

is_gaze_data_getted = False

def gaze_data_callback(gaze_data):
    global is_gaze_data_getted

    print('callback')
    right_gaze_data = gaze_data['right_gaze_point_on_display_area']
    left_gaze_data = gaze_data['left_gaze_point_on_display_area']

    gaze_x = (right_gaze_data[0] +
                     left_gaze_data[0]) / 2.0 * SCREEN_WIDTH
    gaze_y = (right_gaze_data[1] +
                     left_gaze_data[1]) / 2.0 * SCREEN_HEIGHT
    
    is_gaze_data_getted = True
    print(gaze_x, gaze_y)


if __name__ == '__main__':
    # 視線データを取得するとgaze_data_callback()を呼ぶ
    my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA,
                               gaze_data_callback, as_dictionary=True)

    while True:
        if(is_gaze_data_getted):
            is_gaze_data_getted = False
