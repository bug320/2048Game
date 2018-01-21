# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
GRAY = (0xCC, 0xCC, 0xCC)

FONT_TYPE_HEITI = "SimHei"

ID_bg_img = 0x0000
ID_center_img = 0x0001

PATH_IMGS = {ID_bg_img:("img/背景图片.png",0,0),ID_center_img:("img/中心区域.png",46,37)}

class Text(object):
    """
    中文现实问题有两个方面；
    1. 支持中文字体
    2. 传入 unicode字符

    """

    def __init__(self,fontsize=24, fontcolor=WHITE, fonttype=FONT_TYPE_HEITI, issys=True):
        if not py.font:
            py.font.init()
        self.color = fontcolor
        if issys:
            self.font = py.font.SysFont(fonttype,fontsize)
        else:
            self.font = py.font.Font(fonttype,fontsize)
        pass
    def gettextpad(self,msg):
        self.msg = msg
        self.text = self.font.render(msg,1,self.color)
        return self.text
        pass
    def __call__(self,msg=None):
        self.msg = msg if msg else self.msg
        if not self.msg:
            raise Exception("not msg to render")
        return self.gettextpad(self.msg)
        pass
    pass

class Block(py.sprite.Sprite):
    def __init__(self, color, width, height):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pass

class PyClass():
    def __init__(self,ipath):
        py.init()
        py.font.init()

        self.imgs = {}
        self.bgimgs = {}
        for ikey, ipath in ipath.items():
            p,x,y = ipath
            self.bgimgs[ikey] = (py.image.load(p),x,y)
        pass
    def init(self, w, h, title):
        self.wpos = w
        self.hpos = h
        self.screen = py.display.set_mode((self.wpos, self.hpos))
        py.display.set_caption(title)
        pass

    def load_img(self, id, fp):
        img = py.image.load(fp)
        self.imgs[id] = (img, 0, 0)
        pass

    def events(self):
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
        pass

    def update_state(self, func=None):
        for k,pack_img in self.bgimgs.items():
            img,x,y = pack_img
            self.screen.blit(img, (x,y))
        if func is not None:
            func()
        pass

    def render_draw(self):
        py.display.update()
        pass

    def draw_3(self):
        pass

    def font(self):
        text = Text(fontsize=32)(u"2048 Game")
        text2 = Text()(u"联网对抗版本")
        textpos = text.get_rect(x=425,y=85)
        textpos2 = text2.get_rect(x=textpos.x,y=textpos.y+textpos.h)
        self.screen.blit(text, textpos)
        self.screen.blit(text2, textpos2)
        pass
    pass


def run():
    app = PyClass(PATH_IMGS)
    app.init(1000, 618, "2048")
    # app.load_img(0, "img/u001.png")
    while True:
        app.events()
        app.update_state(app.font)
        app.render_draw()


if __name__ == '__main__':
    run()



