import pygame
import sys
from Flappy_Bird.HighScore import Highscore
from Flappy_Bird.Scenes.Scene import Scene
from Flappy_Bird.Shared.GameConstants import GameConstants
from pygame.locals import *

class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)
        self.__game = game
        self.__playername = ""

    def render(self):

        pygame.mouse.set_visible(1)
        self.__game.screen.fill((0,0,0))
        self.__game.screen.blit(pygame.image.load(GameConstants.SPRITE_GAMEOVER), (0, GameConstants.SCREEN_SIZE[1]/2 - GameConstants.GAMEOVER_SIZE[1]/2))
        self.clearText()
        self.addText("Your name: ", 70, GameConstants.SCREEN_SIZE[1]/2 + GameConstants.GAMEOVER_SIZE[1]/2 + 30, size=25)
        self.addText(self.__playername, 170, GameConstants.SCREEN_SIZE[1]/2 + GameConstants.GAMEOVER_SIZE[1]/2 + 30, size=25)
        super(GameOverScene, self).render()

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key >= 65 and event.key <= 122 and len(self.__playername) <= 12:
                    self.__playername += chr(event.key)
                elif event.key == K_RETURN :
                    Highscore().add(self.__playername, self.__game.getScore())
                    self.__game.resetgame()
                    self.__playername = ""
                    self.__game.changeScene(GameConstants.HIGHSCORE_SCENE)
                elif event.key == K_BACKSPACE :
                    l = list(self.__playername)
                    if len(l) > 0 :
                        l.pop(-1)
                    self.__playername = ""
                    for c in l:
                        self.__playername += c