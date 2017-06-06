# camera.py

import cv2


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture('rtsp://admin:admin@10.0.17.13:80')
        # self.frames = cv2.VideoCapture('http://10.10.10.149:8080/video')
        # self.frames = cv2.VideoCapture('rtsp://admin:admin@10.0.17.13:80/live')
        # self.frames = cv2.VideoCapture('http://admin:admin@10.0.17.13:80/axis-cgi/mjpg/video.cgi')
        # self.frames = cv2.VideoCapture('http://admin:admin@10.0.17.13:80/axis-cgi/mjpg/video.cgi?camera=1')
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()