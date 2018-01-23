# -*- coding:utf-8 -*-
# import sys
# import pygame as py
# from pygame import *
from const_var import *


class Singletion(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(Singletion,cls)
            cls._instance = org.__new__(cls, *args, **kwargs)
        return cls._instance
    pass


class Events(Singletion):
    def listener(self):
        for event in py.event.get():
            self.event = event
        pass
    def exit(self):
        if self.noevent():
            return
        if self.event.type == QUIT:
            py.quit()
            sys.exit()
        pass
    def noevent(self):
        return not hasattr(self,"event")
        pass
    def __call__(self):
        return self.event
        pass
    pass

mEvents = Events()

if __name__ == '__main__':
    pass