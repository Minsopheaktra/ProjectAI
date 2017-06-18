from random import randint
import time


class MyPerson:
	tracks = []

	def __init__(self, i, xi, yi, max_age):
		self.i = i
		self.x = xi
		self.y = yi
		self.tracks = []
		self.R = randint(0, 255)
		self.G = randint(0, 255)
		self.B = randint(0, 255)
		self.done = False
		self.state = '0'
		self.age = 0
		self.max_age = max_age
		self.dir = None
		self.notified = False

	def getRGB(self):
		return (self.R, self.G, self.B)

	def getTracks(self):
		return self.tracks

	def getId(self):
		return self.i

	def getState(self):
		return self.state

	def getDir(self):
		return self.dir

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def updateCoords(self, xn, yn):
		self.age = 0
		self.tracks.append([self.x, self.y])
		self.x = xn
		self.y = yn

	def setDone(self):
		self.done = True

	def timedOut(self):
		return self.done

	def going_UP(self, mid_start, mid_end):
		if len(self.tracks) >= 2:
			if self.state == '0':
				if self.tracks[-1][1] < mid_end and self.tracks[-2][1] >= mid_end:  # cruzo la linea
					state = '1'
					self.dir = 'up'
					return True
			else:
				return False
		else:
			return False

	def going_DOWN(self, mid_start, mid_end):
		if len(self.tracks) >= 2:
			if self.state == '0':
				if self.tracks[-1][1] > mid_start and self.tracks[-2][1] <= mid_start:  # cruzo la linea
					state = '1'
					self.dir = 'down'
					return True
			else:
				return False
		else:
			return False

	def age_one(self):
		self.age += 1
		if self.age > self.max_age:
			self.done = True
		return True

	def going_IN(self, left, right, top, bottom):
		if len(self.tracks) >= 2:
			# print(self.state)
			if self.state == '0':
				if self.tracks[-1][1] >= top and self.tracks[-1][1] <= bottom and self.tracks[-1][0] >= left and \
								self.tracks[-1][0] <= right:  # cruzo la linea
					self.state = '1'
					# print('state')
					self.dir = 'in'
					return True
			else:
				return False
		else:
			return False

	def checkArea(self, left, right, top, bottom):
		if self.x > left and self.x < right:
			if self.y > top and self.y < bottom:
				return True
			else:
				return False
		else:
			return False

	# def checkInArea(self, cx, cy):
	# 	if self.x >  and self.x < right:
	# 		return True
	# 	else:
	# 		return False


class MultiPerson:
	def __init__(self, persons, xi, yi):
		self.persons = persons
		self.x = xi
		self.y = yi
		self.tracks = []
		self.R = randint(0, 255)
		self.G = randint(0, 255)
		self.B = randint(0, 255)
		self.done = False
