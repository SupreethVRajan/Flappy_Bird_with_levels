import pygame
import random
from Flappy_Bird.PipeDown import PipeDown
from Flappy_Bird.PipeUp import PipeUp
from Flappy_Bird.Shared import *

class NewPipeSet:

    def __init__(self):
        
        offset = GameConstants.SCREEN_SIZE[1]/3
        ydown = offset + random.randrange(GameConstants.PIPE_SIZE[1]/10, int(GameConstants.SCREEN_SIZE[1] - GameConstants.BASE_SIZE[1] - GameConstants.PIPE_SIZE[1]/10 - offset))
        yup = GameConstants.PIPE_SIZE[1] - ydown + offset

        self.pipes = [
        PipeDown((GameConstants.SCREEN_SIZE[0], ydown), pygame.transform.rotate(pygame.image.load(GameConstants.SPRITE_PIPE), 360), self),
        PipeUp((GameConstants.SCREEN_SIZE[0], -yup), pygame.transform.rotate(pygame.image.load(GameConstants.SPRITE_PIPE), 180), self)
        ]

    def getPosition(self):
        return self.pipes[0].getPosition()

    def getPipes(self):
        return self.pipes

    def updatePosition(self,multiplier):
        for pipe in self.pipes:
            pipe.updatePosition(multiplier)