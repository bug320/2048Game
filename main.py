# -*- coding:utf-8 -*-
import curses


class Frame(object):
    def __init__(self, x, y, w, h):
        self.stdscr=curses.initstr()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pass

    def init(self):
        self.stdscr = curses.newwin()1
        pass

    def load(self):
        pass

    def handle_event(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def close(self):
        pass

    pass
