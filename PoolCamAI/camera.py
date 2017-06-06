# camera.py

import cv2
from time import time

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


class SnapShot(object):
    def __init__(self):
        # Camera 0 is the integrated web cam on my netbook
        camera_port = 'rtsp://admin:admin@10.0.17.13:80/'

        # Number of frames to throw away while the camera adjusts to light levels
        # ramp_frames = 30

        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        self.camera = cv2.VideoCapture(camera_port)


    # Captures a single image from the camera and returns it in PIL format
    def get_image(self):
        cap = SnapShot()
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = cap.camera.read()
        return im

    def get_shot(self):
        temp = SnapShot()
        # temp.get_image()
        # Ramp the camera - these frames will be discarded and are only used to allow v4l2
        # to adjust light levels, if necessary
        for i in range(30):
            temp.get_image()
        print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = self.get_image()
        file = "test_image.png"
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)
        print("success")
        view = cv2.imread('/test_image.png',1)
        cv2.imshow('Preview', view)
        cv2.waitKey(1000)
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        del self.camera

if __name__ == '__main__':
    x = SnapShot()
    x.get_shot()