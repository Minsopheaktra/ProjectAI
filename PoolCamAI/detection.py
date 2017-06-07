import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression


def detection(image=None):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = imutils.resize(image, width=min(400, image.shape[1]))

    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    if len(pick)>0:
        print("[INFO]: {} after suppression".format(len(pick)))
    # We are using Motion JPEG, but OpenCV defaults to capture raw images,
    # so we must encode it into JPEG in order to correctly display the
    # video stream.
    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg