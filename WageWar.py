 import pygame, sys, math, random
from Ball import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [138, 138, 138]

balls = [Ball("Ball/fire.png", [3, 1], [50,100], 30),
        Ball("Ball/it.png", [2, 4], [200,25], 20),
        Ball("Ball/FaZe_Doge.png", [4, 3], [400,400], 10),
        Ball("Ball/FaZe_Doge.png", [10, 3], [300,200], 20),
        Ball("Ball/it.png", [3, 4], [150,200], 30),
        Ball("Ball/FaZe_Doge.png", [3, 6], [200,300], 40),
        Ball("Ball/fire.png", [3, 1], [70,100], 10),
        Ball("Ball/itsboogie2988.png", [3, 5], [300,400], 40)]
        
player=PlayerBall("Ball/it.png", [ width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()   
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
         
    print "??"
    
    for ball in balls:
        ball.move()
        ball.wallBounce(size)
        
    player.move()
    player.wallBounce(size)
    
    for attacker in balls:
        player.ballBounce(attacker)
        attacker.ballBounce(player)
        for defender in balls:
            if attacker != defender:
                attacker.ballBounce(defender)
                
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
        
    
    screen.fill (bgColor)        
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image,player.rect)
    pygame.display.flip()
    clock.tick(60)
    
