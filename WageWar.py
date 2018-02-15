import pygame,sys,math,random
from Ball import *
from PlayerBall import *
from Prop import *
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [138, 138, 138]


while True:
    balls = [Ball("Ball/fire.png", [3, 1], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/it.png", [2, 4], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/FaZe_Doge.png", [4, 3], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/FaZe_Doge.png", [10, 3], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/it.png", [3, 4], [random.randint(0,width),random.randint(0,height)], random.randint(5, 50)),
            Ball("Ball/FaZe_Doge.png", [3, 6], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/fire.png", [3, 1], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/itsboogie2988.png", [4, 7], [random.randint(0,width),random.randint(0,height)], random.randint(10, 50)),
            Ball("Ball/FaZe_Doge.png",  [10, 3],    [300,200],  20),
            Ball("Ball/it.png",         [1, 3],     [70,200],   20),
            Ball("Ball/FaZe_Doge.png",  [7, 8],     [30,70],    20),
            Ball("Ball/FaZe_Doge.png",  [7, 8],     [30,70],    20),
            Ball("Ball/fire.png",       [3, 10],    [70,20],    10),
            Ball("Ball/itsboogie2988.png", [7, 2],  [300,400],  10),
            Ball("Ball/Arch.png",          [4, 2],  [500,500],  40)]
        
    player=PlayerBall("Ball/it.png", [ width/2, height/2])
    
    maxProps = 15
    propsOdds = 75
    props = []
    backgroundImage = pygame.image.load("Backgrounds/main.png")
    backgroundImage = pygame.transform.scale(backgroundImage, size)
    backgroundRect = backgroundImage.get_rect()
    while player.living:
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
             
        if len(props) < maxProps:
            if random.randint(0,100)< propsOdds:
                props += [Prop([random.randint(0, width), random.randint(0,height)])]
        
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
        screen.blit(backgroundImage, backgroundRect)
        for prop in props:
            screen.blit(prop.image, prop.rect)      
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        screen.blit(player.image,player.rect)
        pygame.display.flip()
        clock.tick(60)
    
    
    
    
