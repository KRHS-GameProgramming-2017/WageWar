import pygame, math
from Ball import *


class PlayerBall(Ball):
    def __init__(self, image, pos = [0,0]):
        Ball.__init__(self,image,[0,0],pos,25)
        self.maxSpeed = 8
    
    def wallBounce(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            self.move()
            self.speed[0] = 0
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1]  = -self.speed[1]
            self.move()
            self.speed[1] = 0
            
        
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
