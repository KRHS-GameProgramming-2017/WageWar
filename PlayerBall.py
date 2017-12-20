import pygame, math
from Ball import *


class PlayerBall(Ball):
    def __init__(self, image, pos = [0,0]):
        Ball.__init__(self,image,[0,0],pos,[25,25])
    if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				player.go("up")
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				player.go("down")
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				player.go("left")
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				player.go("right")
            if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				player.go("stop up")
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				player.go("stop down")
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				player.go("stop left")
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				player.go("stop right")
	
	player.move()
	player.wallBounce(size)
	

    
        
