from config import *

class Enemy:
	def __init__(self, x, y, level):
		self.x = x
		self.y = y
		self.level = level
		self.width = 50
		self.height = 50
		self.health = 2
		self.defense = 2

	def draw(self):
		pushMatrix()
		fill(0, 200, 0)
		rect(self.x, self.y, self.width, self.height)
		popMatrix()

	def move(self):
		pass

	def attack(self):
		pass

	def checkCollisions(self):
		for i, bullet in enumerate(BULLET_LIST):
			if (bullet.x >= self.x and bullet.x <= self.x + self.width and
				bullet.y >= self.y and bullet.y <= self.y + self.height):
				self.takeDamage(1)
				BULLET_LIST.pop(i)

	def takeDamage(self, amount):
		self.health -= amount