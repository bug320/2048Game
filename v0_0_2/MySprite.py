# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame.locals import *
from const_var import *

def drawSprite(screen,obj,**kwargs):
    screen.blit(*obj(**kwargs))
    pass

class MySprite(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = None  #
        self.rect = None
        pass
    def update(self):
        pass
    def event(self,func):
        raise Exception("not override {}".format(sys._getframe().f_code.co_name))
        pass
    def update_state(self):
        raise Exception("not override {}".format(sys._getframe().f_code.co_name))
        pass
    def draw(self,screen):
        raise Exception("not override {}".format(sys._getframe().f_code.co_name))
        pass
    pass

class Block(object):
    """
    空白 Surface 块
    """
    def __init__(self, wpos, hpos,topleft=(0,0),color=GRAY):
        self.image= py.Surface([wpos, hpos])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=topleft)
        pass
    def __call__(self):
        return (self.image, self.rect)
        pass
    pass

class Text(object):
    def __init__(self, fontsize=24,fontcolor=WHITE,fonttype=FONT_TYPE_KAITI,issys=True):
        if not py.font:
            py.font.init()
        self.color = fontcolor
        if issys:
            self.font = py.font.SysFont(fonttype, fontsize)
        else:
            self.font = py.font.Font(fonttype, fontsize)
        pass

    def _set_msg(self, msg, topleft):
        """
        设置消息
        :param msg:
        :return:
        """
        self.msg = msg
        self.text = self.font.render(msg,1,self.color)
        self.rect = self.text.get_rect(topleft=topleft)
        return (self.text,self.rect)
        pass

    def __call__(self,msg=None,topleft=(0,0),**kwargs):
        self.msg = msg if msg else self.msg
        if kwargs.has_key("msg"):
            self.msg = kwargs["msg"]
        if kwargs.has_key("topleft"):
            topleft = kwargs["topleft"]
        if not self.msg:
            raise Exception("not msg to render")
        return self._set_msg(self.msg,topleft)
        pass
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

def _draw_button(screen):
    drawSprite(screen,Block(100,100))
    pass

def _draw_text(screen):
    drawSprite(screen,Text(),msg=u"你好",topleft=(100,100))
    # suf,rec = Text()("hello")
    # screen.blit(suf,rec)
    pass

if __name__ == '__main__':
    from pyclass import run
    run(_draw_text)
