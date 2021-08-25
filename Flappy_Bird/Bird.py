import pygame

from Flappy_Bird.Shared import *

class Bird(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__isJump = False
        self.__vel = -9
        self.__acc = 1
        self.__minvel = -8
        self.__maxvel = 10
        self.__jumpvel = -8
        super(Bird, self).__init__(position, GameConstants.BIRD_SIZE, sprite)

    def Jumping(self):
        self.__isJump = True

    def updatePosition(self):

        if self.__vel < self.__maxvel and not self.__isJump :
            self.__vel += self.__acc

        if self.__isJump:
            self.__vel = self.__jumpvel
            self.__isJump = False

        pos = self.getPosition()
        if pos[1] > 0:
            self.setPosition( ( pos[0], pos[1] + min(self.__vel , GameConstants.SCREEN_SIZE[1] - GameConstants.BASE_SIZE[1] - pos[1] - GameConstants.BIRD_SIZE[1]) ) )

    def Intersects(self, obj) :
        return self.intersects(obj)