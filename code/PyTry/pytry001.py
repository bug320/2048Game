# -*- coding:utf-8 -*-

import pygame as py
import sys
from pygame.locals import *

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)


"""
http://inventwithpython.com/pygame/chapter2.html#
"""



def enter_main():
    py.init()
    DISPLAYSURF = py.display.set_mode((1000,618))
    py.display.set_caption('2048Game')
    while True:  # main game loop
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
            py.display.update()
    pass

class PyClass():
    def __init__(self):
        self.imgs = {}
        pass

    def init(self, w, h, title):
        self.wpos = w
        self.hpos = h
        self.screen = py.display.set_mode((self.wpos, self.hpos))
        py.display.set_caption(title)
        pass

    def load_img(self,id,fp):
        img = py.image.load(fp)
        self.imgs[id]=(img,0,0)
        pass

    def events(self):
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
        pass
    def update_state(self,func):
        func()
        pass
    def render_draw(self):
        py.display.update()
        pass

    def draw_3(self):
        src,x,y = self.imgs[0]
        self.screen.blit(src,(x,y))
        pass

    pass

def run():
    app = PyClass()
    app.init(1000,618,"2048")
    app.load_img(0,"img/u001.png")
    while True:
        app.events()
        app.update_state(func=app.draw_3)
        app.render_draw()
        pass
    pass

if __name__ == '__main__':
    run()