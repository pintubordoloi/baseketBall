import os
import sys
import random
import pygame

class Ball(object):
	def __init__(self):
		self.rect = pygame.Rect(400, 400, 50, 50)
	
	def move(self, dx, dy):
		print("moving")
		self.rect.x = dx
		self.rect.y = dy

	def freeFall(self, dx, dy):
		print("freeFall")

class Basket(object):
	def __init__(self):
		self.rect = pygame.Rect(1100, 300, 50, 50)


ball = Ball()
basket = Basket()

def runEverything(dx, dy):
	ball.move(dx, dy)

def gravity(dx, dy):
	ball.freeFall(dx, dy)
	
