from flask import Flask, render_template, Response, request
import cv2 as cv
from hsvfilter import HsvFilter
from vision import Vision

switch = 0
live = 0

app = Flask(__name__)
camera = cv.VideoCapture(0)

@app.route("/")
def index():
    return render_template("index.html")

def main():

    if switch == 1:
        while True:
            success,frame=camera.read()
            
            ret,buffer=cv.imencode('.jpg',frame)
            frame=buffer.tobytes()

            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    
    if live == 1:
        success,frame=camera.read()
        while True:
            vision_limestone = Vision("images/zimba2.jpg")

            hsv_filter = HsvFilter(86,255,0,130,255,255,185,0,255,0)

            processed_image = vision_limestone.apply_hsv_filter(frame, hsv_filter)
            rectangles = vision_limestone.find(processed_image, 0.15)
            output_image = vision_limestone.draw_rectangles(frame, rectangles)

            ret,buffer=cv.imencode('.jpg',frame)
            frame=buffer.tobytes()

            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/requests',methods=['POST'])
def tasks():
    global switch,camera,live
    if request.method == 'POST':
        if request.form.get('stop') == 'hattı izle':

            if switch == 1:
                switch=0
                camera.release()
                cv.destroyAllWindows()
                
            else:
                camera = cv.VideoCapture(0)
                switch = 1
                live = 0

        
        if request.form.get('live') == 'ürün tanı':
            
            if live == 1:
                live=0
                camera.release()
                cv.destroyAllWindows()
                
            else:
                camera = cv.VideoCapture(0)
                live = 1
                switch = 0
                

    return render_template('index.html')

@app.route("/video")
def video():
    return Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)