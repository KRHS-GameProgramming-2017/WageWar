import pygame, math

class Ball():
    def __init__(self, image, speed = [0,0], pos = [0,0], size = None):
         self.baseImage = pygame.image.load(image)
         if size:
             self.image = pygame.transform.scale(self.baseImage, [size, size])
             self.size = size
         else:
             self.size = 50
         self.rect = self.image.get_rect(topleft = pos)
         self.speed = [self.speedx,
                       self.speedy] = speed
         self.living = True               
        
    def move(self):
        self.rect.move_ip(self.speed)
        
    def wallBounce(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.left < 0:
            self.rect.left = 1
            self.speed[0] = -self.speed[0]
        elif  self.rect.right > width:
            self.rect.right = width -1
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0:
            self.rect.top = 1
            self.speed[1]  = -self.speed[1]
        elif self.rect.bottom > height:
            self.rect.bottom = height -1
            self.speed[1]  = -self.speed[1]
            
            
    def ballBounce(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.size > other.size:
                    self.size += other.size/2
                    self.image = pygame.transform.scale(self.baseImage, [self.size, self.size])
                    self.rect = self.image.get_rect(center = self.rect.center)
                    
                else:
                    self.living = False;
                
     
                
        

    








