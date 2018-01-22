# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame import *
from const_var import *

class Block(py.sprite.Sprite):
    def __init__(self, color, width, height):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        pass

class Background(py.sprite.Sprite):
    def __init__(self,):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(IMG_bg)
        self.rect = self.image.get_rect(topleft=TL_bg)
        self.image_1 = py.image.load(IMG_center)
        self.rect_1 = self.image.get_rect(topleft=TL_center)
        pass
    def update(self):
        pass
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        screen.blit(self.image_1,self.rect_1)
        pass
    pass

def __text_Block__(screen):
    block = Block(GRAY,122,76)
    block.rect.topleft = (47,197)
    screen.blit(block.image,block.rect)
    block.rect.topleft = (47+150, 197)
    screen.blit(block.image, block.rect)
    pass

if __name__ == '__main__':
    from pyclass import run
    run(__text_Block__)
    # run(Background().draw)
    pass