# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame import *

from const_var import *
class Text(object):
    """
    中文现实问题有两个方面；
    1. 支持中文字体
    2. 传入 unicode字符

    """

    def __init__(self,fontsize=24, fontcolor=WHITE, fonttype=FONT_TYPE_KAITI, issys=True):
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

def __test__(screen):
    text = Text()
    sur = text(u"kaiti：显示文字 Succefully:注意中文必须是 Unicode 编码")
    textpos = sur.get_rect(topleft=(10,10))
    screen.blit(sur,textpos)
    sur = Text(fonttype="vinerhanditc")(u"tahoma：显示文字 Successfully: 注意中文必须是 Unicode 编码")
    screen.blit(sur,sur.get_rect(topleft=(100,100)))
    pass

if __name__ == '__main__':
    from pyclass import run
    run(__test__)
    pass