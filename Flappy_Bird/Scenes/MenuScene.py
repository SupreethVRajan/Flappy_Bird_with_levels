import pygame
import sys
from Flappy_Bird.Scenes.Scene import Scene
from Flappy_Bird.Shared.GameConstants import GameConstants
from pygame.locals import *

class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)

    def render(self):
        game = self.getGame()

        self.clearButtons()
        y = GameConstants.SCREEN_SIZE[1]/3
        self.addButton("Newgame", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, y , GameConstants.SCREEN_SIZE[0]/3, 30, "NEW GAME")
        self.addButton("Quit", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, y + 100, GameConstants.SCREEN_SIZE[0]/3, 30, "QUIT")

        if game.getStartStatus():
            self.addButton("Continue", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, y + 50, GameConstants.SCREEN_SIZE[0]/3, 30, "CONTINUE")            

        game.screen.blit(pygame.image.load(GameConstants.SPRITE_BACK), (0,0))
        game.screen.blit(pygame.image.load(GameConstants.SPRITE_BASE),(GameConstants.SCREEN_SIZE[0] - GameConstants.BASE_SIZE[0], GameConstants.SCREEN_SIZE[1] - GameConstants.BASE_SIZE[1]))
        super(MenuScene, self).render()

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        pygame.mouse.set_visible(1)

        for event in events:
            newgameButton = self.getButton("Newgame")
            quitButton = self.getButton("Quit")
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT or (event.type == MOUSEBUTTONDOWN and quitButton.isOver(pos) ) :
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN and newgameButton.isOver(pos) :
                self.getGame().resetgame()
                self.getGame().changeScene(GameConstants.PLAYING_SCENE)

            if self.isButtonin("Continue"):
                continueButton = self.getButton("Continue")

                if event.type == MOUSEBUTTONDOWN and continueButton.isOver(pos):
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)

                if event.type == pygame.MOUSEMOTION and continueButton.isOver(pos):
                    continueButton.draw(4, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if newgameButton.isOver(pos) :
                    newgameButton.draw(4, (255, 255, 255))

                if quitButton.isOver(pos) :
                    quitButton.draw(4, (255, 255, 255)) 