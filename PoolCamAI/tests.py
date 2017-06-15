import cv2

from PoolCamAI.condetect import ConDetect

cap = cv2.VideoCapture('peopleCounter.avi')
w = cap.get(3)
print(w)
h = cap.get(4)
print(h)

d = ConDetect(h, w)

while cap.isOpened():
	ret, frame = cap.read()
	data = d.detect(frame)
	cv2.imshow('Frame', frame)
