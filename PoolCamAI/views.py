from django.shortcuts import render
from .camera import VideoCamera
from django.http import StreamingHttpResponse
import time
import pyrebase
config = {
    "apiKey": "AIzaSyCm-_F1g8s527boL5zLma5sXuxI2XgT2As",
    "authDomain": "poolcam-62dfb.firebaseapp.com",
    "databaseURL": "https://poolcam-62dfb.firebaseio.com",
    "projectId": "poolcam-62dfb",
    "storageBucket": "poolcam-62dfb.appspot.com",
   "messagingSenderId": "924526053124"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
email = "admin@kit.com"
password = "12345678"

user = auth.sign_in_with_email_and_password(email, password)


db = firebase.database()






def index(request):
    return render(request, 'PoolCamAI/index.html')


def main(request):
    return render(request, 'PoolCamAI/main.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame, num, person = camera.get_frame()
        # print("Num of notification {0}".format(num))

        if num > 0 and person < 2:
            notification(num)
            person += 1

        print("Num of notification {0}".format(num))
        yield b'--frame\r\nContent-Type: image/jpeg\r\nContent-Length: ' + \
              str(len(frame)).encode() + b'\r\n\r\n' + frame + b'\r\n'


def video_feed(resquest):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def snap(request):
    cam = VideoCamera()
    cam.get_shot()
    return render(request, 'PoolCamAI/modalsnapnotify.html')



def notification(num):
    # title = "have people"
    times = time.time()

    # data to save
    data = {
        # "title": title,
        "times": times,
        "num": num
    }

    #Pass the user's idToken to the push method
    results = db.child("users").child("Notification").push(data, user['idToken'])


def notification_view(request):
    results = db.child("users").child("Notification").get(user['idToken'])

    return render(request, 'PoolCamAI/main.html',results)






