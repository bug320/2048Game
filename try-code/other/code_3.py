# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame.locals import *


class Block(py.sprite.Sprite):
    def __init__(self, color, width, height):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        pass

def updateSprite(screen,sprite):
    sprite.update()
    screen.blit(sprite.image,sprite.rect)
    pass

class PyClass(object):
    clock = py.time.Clock()
    def __init__(self):
        pass

    def init(self, w, h, title):
        self.wpos = w
        self.hpos = h
        self.screen = py.display.set_mode((self.wpos, self.hpos))
        py.display.set_caption(title)
        pass

    def update_state(self,func):
        if func:
            func(self.screen)
        pass

    def events(self):
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
        pass

    def render_draw(self):
        PyClass.clock.tick(30)
        py.display.update()
        pass
    pass


def draw_3(screen):
    block = Block((255,0,0),100,100)
    updateSprite(screen, block)
    pass

def run():
    app = PyClass()
    app.init(1000,618,"2048")
    # app.load_img(0,"img/u001.png")
    while True:
        app.events()
        app.update_state(func=draw_3)
        app.render_draw()
        pass
    pass

if __name__ == '__main__':
    run()