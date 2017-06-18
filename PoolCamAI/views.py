from datetime import datetime
from django.shortcuts import render

from PoolCamAI.dashboard import DashCamera
from .camera import VideoCamera
from django.http import StreamingHttpResponse
import time
import pyrebase
from .linemessage import send2line

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
to = 'Uff558f7354df1711368b767a1f588b75'


def index(request):
	return render(request, 'PoolCamAI/index.html')


def main(request):
	return render(request, 'PoolCamAI/main.html')


def gen(camera):
	"""Video streaming generator function."""
	while True:
		frame, num, person = camera.get_frame()
		# print("Num of notification {0}".format(num))
		now = datetime.now().time()
		endstart = now.replace(hour=6, minute=0, second=0, microsecond=0)
		startend = now.replace(hour=22, minute=0, second=0, microsecond=0)
		if not now > endstart and time < startend:
			if person or num > 3:
				camera.get_shotauto(frame)
				if person:
					notification(num)
					print('Detected')
					# person += 1

		# print("Num of notification {0}".format(num))
		yield b'--frame\r\nContent-Type: image/jpeg\r\nContent-Length: ' + \
			  str(len(frame)).encode() + b'\r\n\r\n' + frame + b'\r\n'
		# yield b'--frame\r\nContent-Type: image/jpeg' + b'\r\n\r\n' + frame + b'\r\n'


def video_feed(resquest):
	"""Video streaming route. Put this in the src attribute of an img tag."""
	return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def snap(request):
	cam = VideoCamera()
	cam.get_shot()
	return render(request, 'PoolCamAI/modalsnapnotify.html')


def notification(num):
	# title = "have people"
	times = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	message = 'Detected {0} person at {1}'.format(num,times)
	send2line(to, message)
	# data to save
	data = {
		# "title": title,
		"times": times,
		"num": num
	}

	#Pass the user's idToken to the push method
	results = db.child("users").child("Notification").push(data, user['idToken'])
	# print(results)


def notification_view(request):
	# print('Hi')
	results = db.child("users").child("Notification").get(user['idToken']).val()
	datas = []
	for i, (key, value) in enumerate(results.items()):
		datas.append(value)
		# print(value)
	# print(datas)
	return render(request, 'PoolCamAI/main.html', {'results': datas})


def gen_dash(camera):
	"""Video streaming generator function."""
	while True:
		frame = camera.get_frame()
		yield b'--frame\r\nContent-Type: image/jpeg\r\nContent-Length: ' + \
			str(len(frame)).encode() + b'\r\n\r\n' + frame + b'\r\n'


def dashboard(request, cam_no=0):

	return StreamingHttpResponse(gen_dash(DashCamera(cam_no)), content_type='multipart/x-mixed-replace; boundary=frame')
