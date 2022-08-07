import cv2 as cv
from hsvfilter import HsvFilter
from vision import Vision

image = cv.imread("images/test2.jpeg")
vision_limestone = Vision("images/zimba.jpg")

#uncomment if you want to change color schema
#vision_limestone.init_control_gui()

hsv_filter = HsvFilter(50,0,0,120,255,165,255,0,0,0)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
processed_image = vision_limestone.apply_hsv_filter(image, hsv_filter)
rectangles = vision_limestone.find(processed_image, 0.1)
output_image = vision_limestone.draw_rectangles(image, rectangles)

while(True):

    cv.imshow("Result", image)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')