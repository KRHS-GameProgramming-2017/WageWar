import pygame, math
from Ball import *


class PlayerBall(Ball):
    def __init__(self, image, pos = [0,0]):
        Ball.__init__(self,image,[0,0],pos,25)
        
	if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
			self.move()
			self.speed[0] = 0
		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1]  = -self.speed[1]
			self.move()
			self.speed[1] = 0
			
	def ballBounce(self, other):
		if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				return True
		return False		
		
	def go(self, direction):
		if direction == "up":
			self.speed[1] = -self.maxSpeed
		elif direction == "down":
			self.speed[1] = self.maxSpeed
		elif direction == "right":
			self.speed[0] = self.maxSpeed
		elif direction == "left":
			self.speed[0] = -self.maxSpeed
			
		if direction == "stop up":
			self.speed[1] = 0
		elif direction == "stop down":
			self.speed[1] = 0
		elif direction == "stop right":
			self.speed[0] = 0
		elif direction == "stop left":
			self.speed[0] = 0
