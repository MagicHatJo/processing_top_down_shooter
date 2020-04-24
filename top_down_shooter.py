from config import *
from Player import Player
from EnemyFactory import EnemyFactory

player = Player(WIDTH / 2, HEIGHT / 2)
enemy_factory = EnemyFactory()

def setup():
	size(WIDTH, HEIGHT)
	imageMode(CENTER)
	rectMode(CENTER)

def draw():
	#Setup
	background(0)

	player.controller()
	translate(WIDTH / 2 - player.x, HEIGHT / 2 - player.y)

	#Bullet
	for i, bullet in enumerate(BULLET_LIST):
		if bullet.outOfRange():
			BULLET_LIST.pop(i)
		bullet.move()
		bullet.draw()

	#Player
	player.draw()

	#Enemy
	if len(enemy_factory.enemy_list) < 3:
		enemy_factory.createEnemy(player.x, player.y)
	enemy_factory.checkCollisions()
	enemy_factory.draw()

def mousePressed():
	#37 for leftclick, 39 for right click
	MOUSE[mouseButton] = True

def mouseReleased():
	MOUSE[mouseButton] = False

def keyPressed():
	KEYBOARD[key] = True

def keyReleased():
	KEYBOARD[key] = False