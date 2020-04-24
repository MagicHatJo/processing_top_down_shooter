import math

class Bullet:
	def __init__(self, x, y, vx, vy, speed=5):
		#Position
		self.x = x
		self.y = y
		#Origin
		self.ox = x
		self.oy = y
		#Velocity
		self.vx = vx
		self.vy = vy
		self.speed = speed
		#Dimensions
		self.width = 10
		self.height = 10
		
	def draw(self):
		pushMatrix()
		fill(0, 0, 255)
		ellipse(self.x, self.y, self.width, self.height)
		popMatrix()

	def move(self):
		self.x += self.vx * self.speed
		self.y += self.vy * self.speed

	def outOfRange(self):
		if (abs(self.x - self.ox) > 1000 or
			abs(self.y - self.oy) > 1000):
			return True
		return False