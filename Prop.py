import pygame, math

class Prop(Ball):
    def __init__(self, image, pos = [0,0]):
        Ball.__init__(self,image,[0,0],pos,25)

	def __init__(self, image, speed = [0,0], 
				 pos = [0,0], size = None):
		 self.image = pygame.image.load(image)
		 self.rect = self.image.get_rect(topleft = pos)
		 self.speed = [self.speedx,
					   self.speedy] = speed
