from config import *
from Enemy import Enemy

import random

class EnemyFactory:
	def __init__(self):
		self.enemy_list = []

	def createEnemy(self, x, y):
		for i in range(5):
			self.enemy_list.append(
				Enemy(
					random.randint(x - 1000, x + 1000),
					random.randint(y - 1000, y + 1000),
					10
				)
			)

	def checkCollisions(self):
		for i, enemy in enumerate(self.enemy_list):
			enemy.checkCollisions()
			if enemy.health <= 0:
				self.enemy_list.pop(i)

	def draw(self):
		for enemy in self.enemy_list:
			enemy.draw()