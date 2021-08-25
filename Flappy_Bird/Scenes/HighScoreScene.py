import pygame
import sys
from Flappy_Bird.HighScore import Highscore
from Flappy_Bird.Scenes.Scene import Scene
from Flappy_Bird.Shared.GameConstants import GameConstants
from pygame.locals import *

class HighScoreScene(Scene):

    def __init__(self, game):
        super(HighScoreScene, self).__init__(game)

    def render(self):
        scores = Highscore()

        self.clearText()

        self.addText("HIGH SCORES", 65, 70, size=35)

        x = GameConstants.SCREEN_SIZE[0]/4
        y = GameConstants.SCREEN_SIZE[1]/4

        for score in scores.getScores() :
            self.addText(score[0], x, y, size=25)
            self.addText(str(score[1]), x + 5*25, y, size=25)
            y += 30

        self.clearButtons()
        self.addButton("Newgame", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, y + 30, GameConstants.SCREEN_SIZE[0]/3, 30, "NEW GAME")
        self.addButton("Quit", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, y + 80, GameConstants.SCREEN_SIZE[0]/3, 30, "QUIT")

        super(HighScoreScene, self).render()

    def handleEvents(self, events):
        super(HighScoreScene, self).handleEvents(events)

        for event in events:
            newgameButton = self.getButton("Newgame")
            quitButton = self.getButton("Quit")
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT or (event.type == MOUSEBUTTONDOWN and quitButton.isOver(pos) ) :
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN and newgameButton.isOver(pos) :
                self.getGame().resetgame()
                self.getGame().changeScene(GameConstants.PLAYING_SCENE)


            if event.type == pygame.MOUSEMOTION:
                if newgameButton.isOver(pos) :
                        newgameButton.draw(4, (255, 255, 255))

                if quitButton.isOver(pos) :
                    quitButton.draw(4, (255, 255, 255))