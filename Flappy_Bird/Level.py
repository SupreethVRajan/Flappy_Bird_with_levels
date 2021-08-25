import pygame
from Flappy_Bird.NewPipeSet import NewPipeSet
from Flappy_Bird.Shared.GameConstants import GameConstants
from Flappy_Bird.Assets.levels import levels

class Level:

    def __init__(self, game):
        self.__game = game
        self.multiplier = 1
        self.currentLevel = 0

    def getLevel(self):
        return self.currentLevel
    
    def load(self, level):
        
        self.currentLevel = level
        
        self.multiplier = levels[level]

    def loadNextLevel(self):
        if self.currentLevel <= 5 :
            self.load(self.currentLevel + 1)