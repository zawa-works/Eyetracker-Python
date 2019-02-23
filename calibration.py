import time
import tobii_research as tr
import wx
import cv2
# import subprocess

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]

def execute(eyetracker):
    global time, tr

    if eyetracker is None:
        return

    calibration = tr.ScreenBasedCalibration(eyetracker)

    calibration.enter_calibration_mode()
    print(("Entered calibration mode for eye tracker with serial number {0}.").format(eyetracker.serial_number))

    points_to_calibrate = [(0.5, 0.5), (0.1, 0.1), (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]

    for point in points_to_calibrate:
        print(("Show a point on screen at {0}.").format(point))

        subprocess.call('./DrawPointHSP/' + str(point[0]) + '_' + str(point[1]) + '.exe')

        print(("Collecting data at {0}.").format(point))
        if calibration.collect_data(point[0], point[1]) != tr.CALIBRATION_STATUS_SUCCESS:
            calibration.collect_data(point[0], point[1])

    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print(("Compute and apply returned {0} and collected at {1} points.").\
        format(calibration_result.status, len(calibration_result.calibration_points)))

    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print(("Compute and apply returned {0} and collected at {1} points.").\
        format(calibration_result.status, len(calibration_result.calibration_points)))

    calibration.leave_calibration_mode()
    print("Left calibration mode.")
   
execute(my_eyetracker)