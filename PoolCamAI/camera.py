# camera.py

import cv2
from time import strftime, gmtime
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils.video import WebcamVideoStream

from PoolCamAI.condetect import ConDetect
from PoolCamAI.detection import detection


class VideoCamera(object):
	def __init__(self):
		camera = 'rtsp://admin:admin@10.0.17.13:80/live'
		#######################################################################
		# Camera Options                                                      #
		# My phone IP Cam - 'http://10.10.10.149:8080/video'                  #
		# Webcam - 0                                                          #
		# 'rtsp://admin:admin@10.0.17.13:80/live'                             #
		# 'http://admin:admin@10.0.17.13:80/axis-cgi/mjpg/video.cgi'          #
		# 'http://admin:admin@10.0.17.13:80/axis-cgi/mjpg/video.cgi?camera=1' #
		#######################################################################
		# Using OpenCV to capture from device 0. If you have trouble capturing
		# from a webcam, comment the line below out and use a video file
		# instead.
		# If you decide to use video.mp4, you must have this file in the folder
		# as the main.py.

		# Initialize camera threading and start getting image object to self.vs variable
		self.vs = WebcamVideoStream(src=camera).start()
		# Getting image width and height
		self.W = self.vs.getW()
		self.H = self.vs.getH()
		# Initialize detection program and specify height and width
		self.detect = ConDetect(self.H, self.W)


	def __del__(self):
		# self.video.release()
		self.vs.stop()

	def get_frame(self):
		# Reading image from camera using threading technique
		image = self.vs.read()

		# # Detecting then streaming
		# data = self.detect.detect(image)
		# if not data['jpeg'] is None:
		# 	return data['jpeg'].tobytes(), data['num'], data['personflag']
		# else:
		# 	return image.tobytes()

		# Streaming from webcam directly
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes(), 0, False

	# No longer used. Reason: Too slow and have redundancy.
	# Keep it in case user want to take snapshot without detection border in frame
	def get_shot(self):
		# Naming snapshot file
		filename = "snap_{0}.jpg".format(strftime("%b_%d_%Y_%H_%M", gmtime()))
		# Reading image from camera using threading technique
		image = self.vs.read()
		# Writing image to file with filename
			# Return true on success and false otherwise
		flag = cv2.imwrite(filename, image)
		# Print to console for Dev
		if flag:
			print(filename, ' was saved successfully on ', strftime("%c"))
		else:
			print(filename, ' was saved unsuccessfully on ', strftime("%c"))

	def get_shotauto(self, image):
			# Naming snapshot file
			filename = "snap_{0}.jpg".format(strftime("%b_%d_%Y_%H_%M_%S", gmtime()))
			# Converting image from binary string format to array
			image = np.asarray(bytearray(image), dtype=np.uint8)
			# Decoding image with color
			image = cv2.imdecode(image, cv2.IMREAD_COLOR)
			# Writing image to file with filename
				# Return true on success and false otherwise
			flag = cv2.imwrite(filename, image)
			# Print to console for Dev
			if flag:
				print(filename, ' was saved successfully on ', strftime("%c"))
			else:
				print(filename, ' was saved unsuccessfully on ', strftime("%c"))
