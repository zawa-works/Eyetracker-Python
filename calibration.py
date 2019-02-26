import time
import tobii_research as tr
import wx
import cv2

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]


def draw_caribration_points(point):
    img_file_name = 'img/image' + str(point[0]) + '_' + str(point[1]) + '.png'
    img = cv2.imread(img_file_name)
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(
        'screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('screen', img)
    cv2.waitKey(2500)


def execute(eyetracker):
    global time, tr

    if eyetracker is None:
        return

    calibration = tr.ScreenBasedCalibration(eyetracker)

    calibration.enter_calibration_mode()
    print(("Entered calibration mode for eye tracker with serial number {0}.").format(
        eyetracker.serial_number))

    points_to_calibrate = [(0.5, 0.5), (0.1, 0.1),
                           (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]

    for point in points_to_calibrate:
        print(("Show a point on screen at {0}.").format(point))
        draw_caribration_points(point)

        print(("Collecting data at {0}.").format(point))
        if calibration.collect_data(point[0], point[1]) != tr.CALIBRATION_STATUS_SUCCESS:
            calibration.collect_data(point[0], point[1])

    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print(("Compute and apply returned {0} and collected at {1} points.").
          format(calibration_result.status, len(calibration_result.calibration_points)))

    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print(("Compute and apply returned {0} and collected at {1} points.").
          format(calibration_result.status, len(calibration_result.calibration_points)))

    calibration.leave_calibration_mode()
    print("Left calibration mode.")


if __name__ == "__main__":
    execute(my_eyetracker)
    exit()
