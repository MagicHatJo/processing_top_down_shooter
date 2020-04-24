from config import *
from Bullet import Bullet
from Missile import Missile

import math
import time

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 50
		self.height = 50
		self.speed = 10
		self.pre_time = 0
		self.interval = 0.15
	
	def draw(self):
		pushMatrix()
		translate(self.x, self.y)
		rotate(math.atan2(mouseY - HEIGHT / 2, mouseX - WIDTH / 2) + HALF_PI)
		fill(255, 255, 255)
		triangle(0, -(self.height / 2), self.height / 2, self.height / 2, -(self.height / 2), self.height / 2)
		popMatrix()
	
	def controller(self):
		if 37 in MOUSE and MOUSE[37]:
			self.shoot("bullet")
		if 39 in MOUSE and MOUSE[39]:
			self.shoot("missile")
		if "w" in KEYBOARD and KEYBOARD["w"]:
			self.y -= self.speed
		if "s" in KEYBOARD and KEYBOARD["s"]:
			self.y += self.speed
		if "a" in KEYBOARD and KEYBOARD["a"]:
			self.x -= self.speed
		if "d" in KEYBOARD and KEYBOARD["d"]:
			self.x += self.speed

	def shoot(self, ammo):
		dx = mouseX - WIDTH / 2
		dy = mouseY - HEIGHT / 2
		length = (dx ** 2 + dy ** 2) ** 0.5
		dx /= length
		dy /= length
		if time.time() - self.pre_time >= self.interval:
			if ammo == "bullet":
				BULLET_LIST.append(Bullet(self.x, self.y, dx, dy))
			if ammo == "missile":
				BULLET_LIST.append(Missile(self.x, self.y, dx, dy))
			self.pre_time = time.time()