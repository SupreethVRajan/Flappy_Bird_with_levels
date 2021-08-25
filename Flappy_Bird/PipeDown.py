from Flappy_Bird.Shared import *

class PipeDown(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__vel = -4

        super(PipeDown, self).__init__(position, GameConstants.PIPE_SIZE, sprite)

    def updatePosition(self, multiplier):
        self.setPosition([self.getPosition()[0] + self.__vel*multiplier, self.getPosition()[1]])