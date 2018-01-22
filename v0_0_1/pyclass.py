# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame import *

from events import  *
from const_var import *
from block import *
from button import *

class PyClass():
    clock = py.time.Clock()
    def __init__(self):
        py.init()

        pass

    def init(self, w, h, title):
        """
        创建主体窗口
        :param w: 窗口的宽
        :param h: 窗口的高
        :param title: 敞口的标题
        :return: None
        """
        self.wpos = w
        self.hpos = h
        self.screen = py.display.set_mode((self.wpos, self.hpos))
        py.display.set_caption(title)
        pass

    def update_state(self, func=None):
        """
        更新表面
        :param func:响应函数
        :return: None
        """
        Background().draw(self.screen)
        if func is not None:
            func(self.screen)
        pass

    def events(self):
        """
        事件处理接口
        :return:None
        """
        mEvents.listener()  #开启监听
        mEvents.exit()
        pass

    def render_draw(self):
        """
        更新表面
        :return:
        """
        PyClass.clock.tick(FTP)
        py.display.update()
        pass

    pass

def run(func=None):
    """
    用于测试
    :param func:
    :return:
    """
    app = PyClass()
    app.init(1000,618,"2048")
    while True:
        app.events()
        app.update_state(func=func)
        app.render_draw()
        pass
    pass

def AppRun(func=None):
    app = PyClass()
    app.init(1000,618,"2048")

    while True:
        app.events()
        app.update_state(func=func)
        app.render_draw()
        pass
    pass

if __name__ == '__main__':
    AppRun(MainButtons().draw)
    pass
