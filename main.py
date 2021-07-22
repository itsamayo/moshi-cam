#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import threading
import os

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceSecret.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pi-office-d68fc-default-rtdb.firebaseio.com',    
})

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    cool_temp, cool_humidity, warm_temp, warm_humidity = getTempData()    
    return render_template('index.html', cool_temp=cool_temp, cool_humidity=cool_humidity, warm_temp=warm_temp, warm_humidity=warm_humidity) #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:        
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')        

def getTempData():
    ref = db.reference('/pi')
    cool_temp = ref.get()['dht_moshi_coolside']['module_info']['last_temp']    
    cool_humidity = ref.get()['dht_moshi_coolside']['module_info']['last_humidity']    
    warm_temp = ref.get()['dht_moshi_warmside']['module_info']['last_temp']    
    warm_humidity = ref.get()['dht_moshi_warmside']['module_info']['last_humidity']    
    return cool_temp, cool_humidity, warm_temp, warm_humidity

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False, port=5001)
    


