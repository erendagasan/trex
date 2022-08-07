import cv2 as cv
from hsvfilter import HsvFilter
from vision import Vision


wincap = cv.VideoCapture(0)

vision_limestone = Vision("images/zimba.jpg")

vision_limestone.init_control_gui()

while(True):
    _, frame = wincap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    screenshot = frame

    screenshot = vision_limestone.apply_hsv_filter(screenshot)

    cv.imshow("Result", screenshot)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')