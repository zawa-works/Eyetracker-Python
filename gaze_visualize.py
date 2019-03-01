#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import tobii_research as tr
from win32api import GetSystemMetrics
import socket

found_eyetrackers = tr.find_all_eyetrackers()  # アイトラッカーを見つける
my_eyetracker = found_eyetrackers[0]  # その中から0番目のアイトラッカーに接続する

host = "127.0.0.1"  # Processingで立ち上げたサーバのIPアドレス
port = 5000  # Processingで設定したポート番号

gaze_data_string = ''

# PCのスクリーンの解像度を取得
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

hasNewGazeData = False


def gaze_data_callback(gaze_data):
    global gaze_data_string

    right_gaze_data = gaze_data['right_gaze_point_on_display_area']
    left_gaze_data = gaze_data['left_gaze_point_on_display_area']

    real_gaze_x = (right_gaze_data[0] +
                   left_gaze_data[0]) / 2.0 * SCREEN_WIDTH
    real_gaze_y = (right_gaze_data[1] +
                   left_gaze_data[1]) / 2.0 * SCREEN_HEIGHT

    gaze_data_string = str(real_gaze_x) + ',' + str(real_gaze_y) + '\n'
    socket_client.send(gaze_data_string.encode('utf-8'))

if __name__ == '__main__':
    my_eyetracker.subscribe_to(
        tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    socket_client = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # オブジェクトの作成
    socket_client.connect((host, port))

    while True:
        print(gaze_data_string)