# camera.py

import cv2
from time import strftime, gmtime
import numpy as np
from imutils.video import WebcamVideoStream

class DashCamera(object):
	def __init__(self, cam_no=0):
		camera = ['rtsp://admin:admin@10.0.17.3:80/live', 'rtsp://admin:admin@10.0.17.13:80/live']
		no = int(cam_no)
		cam = camera[no]
		self.vs = WebcamVideoStream(src=cam).start()

	def __del__(self):
		self.vs.stop()

	def get_frame(self):
		image = self.vs.read()
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()
