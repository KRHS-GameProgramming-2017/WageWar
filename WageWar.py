import pygame, sys, math, random
from Ball import *
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [138, 138, 138]

balls = [Ball("Ball/fire.png", [3, 1], [0,0], [30,30])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    for ball in balls:
        ball.move()
        ball.wallBounce(size)
        
        
            
            
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)
