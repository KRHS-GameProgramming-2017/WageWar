import pygame, math
from Ball import *


class PlayerBall(Ball):
    def __init__(self, image, pos = [0,0]):
        Ball.__init__(self,image,[0,0],pos,25)
        
