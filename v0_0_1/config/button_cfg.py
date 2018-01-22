# -*- coding:utf-8 -*-
from .. import const_var as cv

area = "area"
color = "color"
text = "text"
fire = "fire"

pos = {
    cv.MODEL_WEB: {
        area:(47,197,122,76),
        color:cv.GRAY,
        text:u"联网对抗",
        fire:None
    },  # 联网对抗
    cv.MODEL_LOCAL: {
        area: (439, 197, 122, 76),
        color: cv.GRAY,
        text: u"离线练习",
        fire: None
    },  # 离线练习
    cv.MODEL_HELP: {
        area: (831, 197, 122, 76),
        color: cv.GRAY,
        text: u"游戏帮助",
        fire: None
    },  # 帮助
    cv.MODEL_SET: {
        area: (47, 345, 122, 76),
        color: cv.GRAY,
        text: u"设置",
        fire: None
    },  # 设置
    cv.MODEL_LIST: {
        area: (243, 345, 122, 76),
        color: cv.GRAY,
        text: u"排行榜",
        fire: None
    },  # 排行榜
    cv.MODEL_BACKPACK: {
        area: (439, 345, 122, 76),
        color: cv.GRAY,
        text: u"背包",
        fire: None
    },  # 背包
    cv.MODEL_STORE: {
        area: (635, 345, 122, 76),
        color: cv.GRAY,
        text: u"商城",
        fire: None
    },  # 商城
    cv.MODEL_EXIT:{
        area: (831, 345, 122, 76),
        color: cv.GRAY,
        text: u"退出",
        fire: None
    }  # 退出按钮
}