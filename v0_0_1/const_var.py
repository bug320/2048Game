# -*- coding:utf-8 -*-
import sys
import pygame as py
from pygame import *

# ----- 循环控制 -----
FTP = 30 # 刷新频率

FONT_TYPE_HEITI = "SimHei"  # 字体类型
FONT_TYPE_KAITI = "kaiti"  # 字体类型
FONT_TYPE_LISU = "lisu"  # 字体类型
FONT_TYPE_FANGSONG = "fangsong"  # 字体类型

# ----- 颜色定义 -----

BLACK = (  0,   0,   0)   # 黑色
WHITE = (255, 255, 255)   # 白色
RED = (255,   0,   0)     # 红色
GREEN = (  0, 255,   0)   # 绿色
BLUE = (  0,   0, 255)    # 蓝色
GRAY = (0xCC, 0xCC, 0xCC) # 灰色

# ----- 图片资源 -------

# 背景图片
IMG_bg = "img/bg.png"            # 背景图片（边框）
TL_bg = (0,0)
IMG_center = "img/center.png"   #  中心显示区域
TL_center = (46,37)

# 技能
ACTION_BIG_DEAD = 0xA001      # 销毁大数
IMG_BIG_DEAD = "img/bigDeadAction.png"
ACTION_RANDOM_NUM = 0xA002    # 随机变化
IMG_RANDOM_NUM = "img/randomAciton.png"
ACTION_BIG_DOWN = 0xA003      # 大数下移
IMG_BIG_DOWN = "img/bigDownAction.png"

IMG_USER = "img/user.png"  # 用户头像



# 模块索引
MODEL_WEB = 0xF001  # 联网对抗模块
MODEL_LOCAL = 0xF002  # 离线练习
MODEL_HELP = 0xF003   # 游戏帮助
MODEL_SET = 0xF004    # 设置
MODEL_LIST = 0xF005     # 排行榜
MODEL_BACKPACK = 0xF006  # 背包
MODEL_STORE = 0xF007     # 商城
MODEL_EXIT = 0xF008      # 退出按钮


if __name__ == '__main__':
    pass