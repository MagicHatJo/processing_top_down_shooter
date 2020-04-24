from config import *
from Bullet import Bullet

import math

class Missile(Bullet):
	def __init__(self, x, y, vx, vy, speed=10):
		Bullet.__init__(self, x, y, vx, vy, speed)
		self.angle = math.atan2(mouseY - HEIGHT / 2, mouseX - WIDTH / 2) + HALF_PI
	
	def draw(self):
		pushMatrix()
		translate(self.x, self.y)
		rotate(self.angle)
		fill(200, 0, 200)
		rect(0, 0, 10, 30)
		popMatrix()