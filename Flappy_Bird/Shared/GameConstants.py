import os
import pygame

class GameConstants:

    SCREEN_SIZE   = [289, 511]
    BG_SIZE       = [288, 512]
    FPS           = 34
    PIPE_SIZE     = [52, 320]
    BIRD_SIZE     = [34, 24]
    BASE_SIZE     = [336, 112]
    GAMEOVER_SIZE = [288, 162]
    NUMBER_SIZE   = [25,36]

    PLAYING_SCENE   = 0
    GAMEOVER_SCENE  = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE      = 3

    SPRITE_BIRD     = os.path.join("Flappy_Bird", "Assets", "bird.png")
    SPRITE_PIPE     = os.path.join("Flappy_Bird", "Assets", "pipe.png")
    SPRITE_BASE     = os.path.join("Flappy_Bird", "Assets", "base.png")
    SPRITE_BACK     = os.path.join("Flappy_Bird", "Assets", "background.png")
    SPRITE_GAMEOVER = os.path.join("Flappy_Bird", "Assets", "gameover.png")
    SPRITE_NUMBERS  =[
        os.path.join("Flappy_Bird", "Assets", "0.png"),
        os.path.join("Flappy_Bird", "Assets", "1.png"),
        os.path.join("Flappy_Bird", "Assets", "2.png"),
        os.path.join("Flappy_Bird", "Assets", "3.png"),
        os.path.join("Flappy_Bird", "Assets", "4.png"),
        os.path.join("Flappy_Bird", "Assets", "5.png"),
        os.path.join("Flappy_Bird", "Assets", "6.png"),
        os.path.join("Flappy_Bird", "Assets", "7.png"),
        os.path.join("Flappy_Bird", "Assets", "8.png"),
        os.path.join("Flappy_Bird", "Assets", "9.png")
    ]

    HIGHSCOREFILE = os.path.join("Flappy_Bird", "highscore.dat")