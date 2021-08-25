import pygame
from Flappy_Bird import *
from Flappy_Bird.Scenes import *
from Flappy_Bird.Shared.GameConstants import GameConstants


class Game:
    def __init__(self):

        self.__score = 0
        self.__level = Level(self)
        self.__start = 0
        self.__level.load(1)
        self.mul = self.__level.multiplier

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Flappy-Bird!!!")
        pygame.display.set_mode()

        self.__bird = Bird( (GameConstants.SCREEN_SIZE[0]/3, GameConstants.SCREEN_SIZE[1]/2) , pygame.image.load(GameConstants.SPRITE_BIRD), self)

        self.__pipes = [
            NewPipeSet()
        ]

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self)
        )

        self.__CurrentScene = GameConstants.MENU_SCENE

        
    def start(self):    
        while 1:
            self.__clock.tick(GameConstants.FPS)
            self.screen.fill((0,0,0))


            self.mul = self.__level.multiplier

            currentScene = self.__scenes[self.__CurrentScene]
            currentScene.render()
            currentScene.handleEvents(pygame.event.get())

            pygame.display.update()

    def changeScene(self, scene):
        self.__CurrentScene = scene

    def getScore(self):
        return self.__score

    def getLevel(self):
        return self.__level

    def increaseScore(self):
        self.__score += self.__level.getLevel()

    def getPipes(self):
        return self.__pipes

    def addPipes(self):
        self.__pipes.append(NewPipeSet())

    def deletePipes(self):
        self.__pipes.pop(0)

    def getBird(self):
        return self.__bird

    def getStartStatus(self):
        return self.__start

    def updateStartStatus(self ,status):
        self.__start = status

    def resetgame(self):
        self.__score = 0
        self.__level = Level(self)
        self.__level.load(1)
        self.__start = 0
        self.mul = self.__level.multiplier
        self.__bird = Bird( (GameConstants.SCREEN_SIZE[0]/3, GameConstants.SCREEN_SIZE[1]/2) , pygame.image.load(GameConstants.SPRITE_BIRD), self)
        self.__pipes = [
            NewPipeSet()
        ]

Game().start()