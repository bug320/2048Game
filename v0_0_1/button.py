# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame import *

from events import  *
from const_var import *
from block import *
from text import *

AREA = "AREA"
COLOR = "COLOR"
TEXT = "TEXT"
FIRE = "FIRE"

models = {
    MODEL_WEB: {
        AREA:(47,197,122,76),
        COLOR:GRAY,
        TEXT:u"联网对抗",
        FIRE:None
    },  # 联网对抗
    MODEL_LOCAL: {
        AREA: (439, 197, 122, 76),
        COLOR: GRAY,
        TEXT: u"离线练习",
        FIRE: None
    },  # 离线练习
    MODEL_HELP: {
        AREA: (831, 197, 122, 76),
        COLOR: GRAY,
        TEXT: u"游戏帮助",
        FIRE: None
    },  # 帮助
    MODEL_SET: {
        AREA: (47, 345, 122, 76),
        COLOR: GRAY,
        TEXT: u"设置",
        FIRE: None
    },  # 设置
    MODEL_LIST: {
        AREA: (243, 345, 122, 76),
        COLOR: GRAY,
        TEXT: u"排行榜",
        FIRE: None
    },  # 排行榜
    MODEL_BACKPACK: {
        AREA: (439, 345, 122, 76),
        COLOR: GRAY,
        TEXT: u"背包",
        FIRE: None
    },  # 背包
    MODEL_STORE: {
        AREA: (635, 345, 122, 76),
        COLOR: GRAY,
        TEXT: u"商城",
        FIRE: None
    },  # 商城
    MODEL_EXIT:{
        AREA: (831, 345, 122, 76),
        COLOR: GRAY,
        TEXT: u"退出",
        FIRE: None
    }  # 退出按钮
}


class MainButtons(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.btns = [ Button(model) for model in models.keys()]
        pass


    def draw(self,screen):
        title = u"2048 Game"
        subTitle = u"联网对抗版"
        title = Text(fontsize=32)(title)
        tlrect = title.get_rect(x=415,y=75)
        subTitle = Text()(subTitle)
        stlrect = title.get_rect(x=456,y=122)
        screen.blit(title,tlrect)
        screen.blit(subTitle,stlrect)
        for btn in self.btns:
            btn.draw(screen)
        pass

    pass

class Button(py.sprite.Sprite):
    def __init__(self,model):
        py.sprite.Sprite.__init__(self)
        self.model = model
        pass

    def abutton(self, model):
        color = models[model][COLOR]
        area = py.Rect(models[model][AREA])
        text = models[model][TEXT]
        tsuf = Text(fontcolor=BLACK)(text)
        bsuf = Block(color, area.w, area.h).image
        brect = bsuf.get_rect(x=area.x, y=area.y)
        trect = tsuf.get_rect()
        trect.x = (brect.w - trect.w) / 2
        trect.y = (brect.h - trect.h) / 2
        # 　bsuf.blit(tsuf,brect)
        bsuf.blit(tsuf, trect)
        return (bsuf, tsuf, brect)
        pass
    def update(self):
        self.event()
        pass
    def event(self):
        if mEvents.noevent():
            return
        if mEvents.event.type == MOUSEBUTTONDOWN:
            pos= py.mouse.get_pos()
            rt = Rect(models[self.model][AREA])
            if rt.collidepoint(pos):
                models[self.model][COLOR] = RED   # ----todo ：测试用句 [debug]
                pass
            pass
        pass
    def draw(self,screen):
        self.update()
        bsuf, tsuf, brect = self.abutton(self.model)
        screen.blit(bsuf, brect)

        pass
    pass

if __name__ == '__main__':
    from pyclass import run
    run(MainButtons().draw)
    # run(Button(MODEL_WEB).draw)
    # Buttons().abutton(MODEL_WEB)
    pass
