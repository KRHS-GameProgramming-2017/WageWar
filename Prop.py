import pygame, math
from Ball import *


class Prop(Ball):
    def __init__(self, pos = [0,0]):
        Ball.__init__(self,"Prop/food.png",[0,0],pos,15)
        
