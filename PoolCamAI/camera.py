# camera.py

import cv2
from time import strftime, gmtime
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils.video import WebcamVideoStream

from PoolCamAI.detection import detection


class VideoCamera(object):
    def __init__(self):
        camera = 'rtsp://admin:admin@10.0.17.13:80/'

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

        # self.video = cv2.VideoCapture('http://192.168.1.106:8080/video')
        self.vs = WebcamVideoStream(src=camera).start()
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
        # initialize the HOG descriptor/person detector

    def __del__(self):
        # self.video.release()
        self.vs.stop()

    def get_frame(self):

        # faceCascade = cv2.CascadeClassifier('D:\AI\ProjectAI\media\haarcascade_fullbody.xml')
        # success, image = self.video.read()
        image = self.vs.read()
        data = detection(image)

        if not data['jpeg'] is None:
            return data['jpeg'].tobytes(), data['num'], data['personflag']
        else:
            return image.tobytes()

    def get_shot(self):
        file = "snap_{0}.jpg".format(strftime("%b_%d_%Y_%H_%M", gmtime()))
        # ret, image = self.video.read()
        image = self.vs.read()
        flag = cv2.imwrite(file, image)
        if flag:
            print('snap saved')

