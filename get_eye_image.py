
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def pause_plot():
    fig, ax = plt.subplots(1, 1)
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.sin(x)
    # 初期化的に一度plotしなければならない
    # そのときplotしたオブジェクトを受け取る受け取る必要がある．
    # listが返ってくるので，注意
    lines, = ax.plot(x, y)

    # ここから無限にplotする
    while True:
        # plotデータの更新
        x += 0.1
        y = np.sin(x)

        # 描画データを更新するときにplot関数を使うと
        # lineオブジェクトが都度増えてしまうので，注意．
        #
        # 一番楽なのは上記で受け取ったlinesに対して
        # set_data()メソッドで描画データを更新する方法．
        lines.set_data(x, y)

        # set_data()を使うと軸とかは自動設定されないっぽいので，
        # 今回の例だとあっという間にsinカーブが描画範囲からいなくなる．
        # そのためx軸の範囲は適宜修正してやる必要がある．
        ax.set_xlim((x.min(), x.max()))
        ax.set_ylim((-0.5, 0.5))

        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(.01)


if __name__ == "__main__":
    pause_plot()

# import time
# import tobii_research as tr
# found_eyetrackers = tr.find_all_eyetrackers()
# my_eyetracker = found_eyetrackers[0]

# with open(filename, "wb") as f:
#     calibration_data = eyetracker.retrieve_calibration_data()
#     if calibration_data is not None:
#         f.write(eyetracker.retrieve_calibration_data())

# display_area = my_eyetracker.get_display_area()
# print(my_eyetracker.retrieve_calibration_data())
# global_eye_image
# def eye_image_callback(eye_image_data):
#     global global_eye_image
#     global_eye_image = eye_image_data
#     # print(eye_image_data)


# def eye_images(eyetracker):
#     # print(("Subscribing to eye images for eye tracker with serial number {0}.").format(eyetracker.serial_number))
#     eyetracker.subscribe_to(tr.EYETRACKER_EYE_IMAGES, eye_image_callback, as_dictionary=True)
#     # Wait for eye images.
#     time.sleep(2)
#     eyetracker.unsubscribe_from(tr.EYETRACKER_EYE_IMAGES, eye_image_callback)
#     # print("Unsubscribed from eye images.")

# def execute(eyetracker):
#     if eyetracker is not None:
#         eye_images(eyetracker)
#     else:
#         print("No tracker with eye images to run example.")

# while True:
#     execute(my_eyetracker)
#     print(global_eye_image)
