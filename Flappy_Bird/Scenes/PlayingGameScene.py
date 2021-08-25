import sys
import pygame
import time
from pygame.locals import *
from Flappy_Bird.Scenes.Scene import Scene
from Flappy_Bird.NewPipeSet import NewPipeSet
from Flappy_Bird.Shared.GameConstants import GameConstants
from Flappy_Bird.HighScore import Highscore

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
        self.__jumpStatus = False
        self.__game = game
        self.__playername = ""
        self.__start = 0
        self.__pipeCount = 0

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()



        if game.getStartStatus() == 0:
            self.__pipeCount = 0

        game.updateStartStatus(1)
        
        self.clearText()
        self.clearButtons()

        game.screen.blit(pygame.image.load(GameConstants.SPRITE_BACK), (0,0))

        if self.__pipeCount == 10:
            if game.getLevel().getLevel() <= 5:
                self.__pipeCount = 0
                game.getLevel().loadNextLevel()
            # else :
            #     self.__start = 0
            #     game.screen.fill((0, 0, 0))
            #     y = GameConstants.SCREEN_SIZE[1]/3
            #     self.addText("CONGRATULATIONS!", 50, y, size=30)
            #     self.addText("GAME CLEARED", 50, y + 50, size=30)
            #     self.addText("Your name: ", 70, y + 100, size=25)
            #     self.addText(self.__playername, 170, y + 100, size=25)

        pygame.mouse.set_visible(0)

        bird = game.getBird()
        if self.__jumpStatus :
            bird.Jumping()

        if self.__start :
            bird.updatePosition()

        self.__jumpStatus = False

        game.screen.blit(bird.getSprite(), bird.getPosition()) 


        pipes = game.getPipes()

        for pipeset in pipes:
            x = bird.getPosition()[0] - pipeset.getPosition()[0]/2 - 40
            if game.getLevel().getLevel() <= 3:
                if x < 2 and x >= 0 :
                    game.increaseScore()
                    self.__pipeCount += 1
            else :
                if x < 4 and x >= 0 :
                    game.increaseScore()
                    self.__pipeCount += 1

        x = 0

        for pipeset in pipes:
            for i in range(2):
                if bird.Intersects(pipeset.getPipes()[i]) :
                    x += 1

        if bird.getPosition()[1] <= 0 or bird.getPosition()[1] + GameConstants.BASE_SIZE[1] + GameConstants.BIRD_SIZE[1] >= GameConstants.SCREEN_SIZE[1] :
            x += 1

        if x:
            game.changeScene(GameConstants.GAMEOVER_SCENE)
            self.__start = 0
            self.__pipeCount = 0
            self.__jumpStatus = False

        if pipes[0].getPosition()[0] + GameConstants.PIPE_SIZE[0] < 0:
            game.deletePipes()

        if pipes[-1].getPosition()[0] + GameConstants.PIPE_SIZE[0]/2 < GameConstants.SCREEN_SIZE[0]/3 :
            game.addPipes()

        for pipeset in pipes:
            game.screen.blit(pipeset.getPipes()[0].getSprite(), pipeset.getPipes()[0].getPosition())
            game.screen.blit(pipeset.getPipes()[1].getSprite(), pipeset.getPipes()[1].getPosition())
            if self.__start :
                pipeset.updatePosition(game.mul)

        game.screen.blit(pygame.image.load(GameConstants.SPRITE_BASE),(GameConstants.SCREEN_SIZE[0] - GameConstants.BASE_SIZE[0], GameConstants.SCREEN_SIZE[1] - GameConstants.BASE_SIZE[1]))

        digits = [ int(x) for x in list(str(game.getScore())) ]
        xoffset = GameConstants.SCREEN_SIZE[0]/2 - GameConstants.NUMBER_SIZE[0]*len(digits)/2

        for digit in digits:
            game.screen.blit(pygame.image.load(GameConstants.SPRITE_NUMBERS[digit]), (xoffset, 50))
            xoffset += GameConstants.NUMBER_SIZE[0]

        self.addButton("Level", (0, 0, 0), GameConstants.SCREEN_SIZE[0]/3, 0, 100, 35, "LEVEL " + str(game.getLevel().getLevel()))

        if self.__pipeCount == 10 and game.getLevel().getLevel() == 6:
            game.screen.fill((0, 0, 0))

        super(PlayingGameScene, self).render()

    def handleEvents(self, events):
        for event in events:

            if self.getGame().getLevel().getLevel() == 6 and self.__pipeCount == 10 :
                if event.type == pygame.QUIT :
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key >= 65 and event.key <= 122 :
                        self.__playername += chr(event.key)
                    elif event.key == K_RETURN :
                        Highscore().add(self.__playername, self.__game.getScore())
                        self.__playername = ""
                        self.__game.updateStartStatus(0)
                        self.__pipeCount = 0
                        self.__game.changeScene(GameConstants.MENU_SCENE)
                    elif event.key == K_BACKSPACE :
                        l = list(self.__playername)
                        if len(l) > 0:
                            l.pop(-1)
                        self.__playername = ""
                        for c in l:
                            self.__playername += c

            else :
                if event.type == pygame.QUIT :
                    sys.exit()
                if event.type == KEYDOWN :
                    if event.key == K_SPACE or event.key == K_UP :
                        self.__jumpStatus = True
                        self.__start = 1
                    if event.key == K_ESCAPE :
                        self.__start = 0
                        self.getGame().changeScene(GameConstants.MENU_SCENE)