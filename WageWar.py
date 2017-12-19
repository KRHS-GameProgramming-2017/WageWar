import pygame, sys, math, random
from Ball import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [138, 138, 138]

balls = [Ball("Ball/fire.png", [3, 1], [0,0], [30,30]),
        Ball("Ball/it.png", [2, 4], [0,0], [20,20]),
        Ball("Ball/FaZe_Doge.png", [4, 3], [0,0], [10,10])]
        
player=PlayerBall("Ball/it.png", [ width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    for ball in balls:
        ball.move()
        ball.wallBounce(size)
        
    player.move()
    player.wallBounce(size)
    
        
     
    screen.fill (bgColor)        
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image,player.rect)
    pygame.display.flip()
    clock.tick(60)
    
