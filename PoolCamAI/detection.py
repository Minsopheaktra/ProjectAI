import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression


def detection(image=None):

    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    if not image is None:
        # resize image to (1) reduce detection time (2) improve detection accuracy
        frame = imutils.resize(image, width=min(400, image.shape[1]))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)

        # apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping
        # boxes that are still people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

        num = len(pick)
        personflag = 0
        if num > 0:
            print("[INFO]: {} people".format(num))
            personflag = 1
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return {'jpeg': jpeg, 'num': num, 'personflag': personflag}
        #
        # def getnum():
        #     print("Get num{0}".format(num))
        #     return num
        #
        # def setnum(n):
        #     print("Set num{0}".format(n))
        #     num = n