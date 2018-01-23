# -*- coding:utf-8 -*-
import pygame as py
from  pygame.locals import *

from const_var import *
from events import mEvents
from MySprite import *


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

class Button(py.sprite.Sprite):
    def __init__(self,model):
        py.sprite.Sprite.__init__(self)
        py.font.init()
        self.model = model
        self.image = None
        self.rect = None
        #self.button()
        pass

    def _button(self):
        """
        制作按钮单个按钮
        :param model: 按钮配置位置
        :return:
        """
        # 获取配置属性
        color = models[self.model][COLOR]
        area = py.Rect(models[self.model][AREA])
        text = models[self.model][TEXT]
        # 制作样式
        # print "-==-=-=-=-=",type(area.w)

        self.image,self.rect = Block(area.w, area.h,topleft=(area.x,area.y),color=color)() # 背景
        text,rect = Text(fontcolor=BLACK)(text)                               # 提示文字
        rect.x = (self.rect.w - rect.w)/2                                     # 设置文字位置
        rect.y = (self.rect.h - rect.h)/2
        self.image.blit(text,rect)# 组合文字和背景
        #print "========",self.rect
        return (self.image,self.rect)
        pass

    def __call__(self):
        return self._button()
        pass

    def update(self):
        pass

    def update_state(self):
        self.event()
        pass

    def event(self):
        if mEvents.noevent():
            return
        if mEvents.event.type == MOUSEBUTTONDOWN:
            pos= py.mouse.get_pos()
           

            if self.rect.collidepoint(pos):
                models[self.model][COLOR] = RED   # ----todo ：测试用句 [debug]
                
                pass
            pass
        pass

    def draw(self,screen):
        self.event()
        drawSprite(screen,self)
        # screen.blit(*self.button())
        # screen.blit(*self())
        pass
    pass


class WebModle(MySprite):
    def __init__(self,):
        self.btns = [Button(model) for model in models]
        pass
    def update(self):
        pass
    def event(self,func=None):
        pass
    def update_state(self):

        pass
    def  draw(self,screen):
        self._draw_buttons(screen)
        self._draw_buttons(screen)
        pass

    def _draw_title(self,screen):
        text,rect = Text(fontsize=32)(u"2048 Game")

        pass
    def _draw_buttons(self,screen):
        for btn in self.btns.values():
            btn.draw(screen)

        pass
    pass

if __name__ == '__main__':
    from pyclass import run
    run(Button(MODEL_WEB).draw)
    pass