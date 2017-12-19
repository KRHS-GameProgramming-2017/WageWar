import pygame, math

class Ball():
    def __init__(self, image, speed = [0,0], pos = [0,0], size = None):
         self.image = pygame.image.load(image)
         if size:
             self.image = pygame.transform.scale(self.image, size)
             self.size = size
         else:
             self.size = 50
         self.rect = self.image.get_rect(topleft = pos)
         self.speed = [self.speedx,
                       self.speedy] = speed
    def move(self):
        self.rect.move_ip(self.speed)
        
    def wallBounce(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0]  = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1]  = -self.speed[1]
            
            
    def ballBounce(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speed[0]  = -self.speed[0]
                self.speed[1]  = -self.speed[1]

    def __init__(self, image, speed = [0,0], pos = [0,0], size = None):
         self.image = pygame.image.load(image)
         if size:
             self.image = pygame.transform.scale(self.image, size)
         self.rect = self.image.get_rect(topleft = pos)
         self.speed = [self.speedx,
                       self.speedy] = speed
    def move(self):
        self.rect.move_ip(self.speed)
        
    def wallBounce(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0]  = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1]  = -self.speed[1]
                        
    def ballBounce(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speed[0]  = -self.speed[0]
                self.speed[2]  = -self.speed[2]









