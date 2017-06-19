# #Contador de personas
# #Federico Mejia
import time

import cv2
import imutils
import numpy as np

from PoolCamAI.Person import MyPerson
from .common import draw_str



class ConDetect:
	def __init__(self, h, w):
		self.people = 0
		self.cnt_in = 0
		self.ih = h
		self.iw = w
		print("{0}, {1}\n".format(self.iw, self.ih))
		self.frameArea = self.ih * self.iw
		# self.areaTH = self.frameArea / 250
		self.areaTH = 500
		self.left = int(2 * (self.iw / 10))
		self.right = int(8 * (self.iw / 10))
		self.top = int(2 * (self.iw / 10))
		self.bottom = int(7 * (self.iw / 10))
		self.leftLimit = int(1 * (self.iw / 10))
		self.rightLimit = int(9 * (self.iw / 10))
		self.topLimit = int(1 * (self.iw / 10))
		self.bottomLimit = int(8 * (self.iw / 10))
		print("{0}, {1}, {2}, {3}".format(self.left, self.right, self.top, self.bottom))
		self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		self.kernelOp = np.ones((3, 3), np.uint8)
		self.kernelCl = np.ones((11, 11), np.uint8)
		self.font = cv2.FONT_HERSHEY_SIMPLEX
		self.persons = []
		self.max_p_age = 5
		self.pid = 1
		self.M = []
		self.cx = 0
		self.cy = 0
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.timer = 0

	def detect(self, image):
		frame = image
		# frame = imutils.resize(image, width=640)

		for i in self.persons:
			i.age_one()
		# self.people = 0

		fgmask = self.fgbg.apply(frame)
		alert = False

		try:
			ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
			mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, self.kernelOp)
			mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernelCl)
		except:
			print('EOF')

		_, contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours0:
			area = cv2.contourArea(cnt)
			# print(area)
			if area > self.areaTH:
				self.M = cv2.moments(cnt)
				self.cx = int(self.M['m10'] / self.M['m00'])
				self.cy = int(self.M['m01'] / self.M['m00'])
				self.x, self.y, self.w, self.h = cv2.boundingRect(cnt)

				new = True

				if self.cy in range(self.topLimit, self.bottomLimit):
					if self.cx in range(self.leftLimit, self.rightLimit):
						for i in self.persons:

							if abs(self.cx - i.getX()) <= self.w and abs(self.cy - i.getY()) <= self.h:
								new = False
								i.updateCoords(self.cx, self.cy)
								if i.going_IN(self.left, self.right, self.top, self.bottom):
									self.cnt_in += 1
									print("ID:", i.getId(), 'went into the pool at', time.strftime('%c'))
									self.timer +=1
									if self.timer == 15:
										self.timer = 0
										alert = True
										self.cnt_in = 0


									# print(i.age)


								# print(self.people)
								break

							if i.getState() == '1':
								if i.getDir() == 'in':
									i.setDone()


							if i.timedOut():
								index = self.persons.index(i)
								self.persons.pop(index)
								del i
								# self.cnt_in -= 1
								# self.pid -= 1
								# print(len(self.persons))

						if new:
							p = MyPerson(self.pid, self.cx, self.cy, self.max_p_age)
							self.persons.append(p)
							self.pid += 1



				cv2.circle(frame, (self.cx, self.cy), 5, (0, 0, 255), -1)
				cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2)
				# cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)

		for i in self.persons:
			cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), self.font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

		str_in = 'IN: ' + str(self.cnt_in)
		str_down = 'People: ' + str(alert)
		ps = 'Persons: ' + str(len(self.persons))
		cv2.rectangle(frame, (self.left, self.top), (self.right, self.bottom), (255, 0, 0), 2)
		cv2.rectangle(frame, (self.leftLimit, self.topLimit), (self.rightLimit, self.bottomLimit), (255, 0, 0), 2)
		cv2.putText(frame, str_in, (10, 40), self.font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
		cv2.putText(frame, str_in, (10, 40), self.font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
		cv2.putText(frame, str_down, (10, 90), self.font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
		cv2.putText(frame, str_down, (10, 90), self.font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
		draw_str(frame, (20, 20), ps)

		# cv2.imshow('Frame', frame)
		# cv2.imshow('Mask', mask)
		# cv2.imwrite('shot.png', frame)
		# return frame
		ret, jpeg = cv2.imencode('.jpg', frame)
		return {'jpeg': jpeg, 'num': self.cnt_in, 'personflag': alert}
