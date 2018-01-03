# -*- coding:utf-8 -*-

import pygame,sys
from pygame.locals import *

"""
http://inventwithpython.com/pygame/chapter2.html#
"""

def enter_main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1000,618))
    pygame.display.set_caption('2048Game')
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
    pass

if __name__ == '__main__':
    enter_main()