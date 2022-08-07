import cv2 as cv
from hsvfilter import HsvFilter
from vision import Vision

wincap = cv.VideoCapture(0)

vision_limestone = Vision("images/zimba.jpg")

#uncomment if you want to change color schema
#vision_limestone.init_control_gui()
hsv_filter = HsvFilter(50,0,0,120,255,165,255,0,0,0)

ret, frame = wincap.read()
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

processed_image = vision_limestone.apply_hsv_filter(frame, hsv_filter)
rectangles = vision_limestone.find(processed_image, 0.1)
output_image = vision_limestone.draw_rectangles(frame, rectangles)


while(True):
    cv.imshow("Result", frame)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')