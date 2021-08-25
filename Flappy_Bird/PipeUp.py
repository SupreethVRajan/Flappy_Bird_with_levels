from Flappy_Bird.Shared import *

class PipeUp(GameObject):

    def __init__(self, position, sprite, game ):
        self.__game = game
        self.__vel = -4

        super(PipeUp, self).__init__(position, GameConstants.PIPE_SIZE, sprite)

    def updatePosition(self, multiplier):
        self.setPosition([self.getPosition()[0] + self.__vel*multiplier, self.getPosition()[1]])