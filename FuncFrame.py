# -*- coding:utf-8 -*-


import curses


# 重要常量
NOT_INIT_GAME = 0x0001   # 初始化失败退出
NOT_LOAD_SRC = 0x0002    # 加载资源失败退出
EXIT_GAME_FLAG = 0x0004  # 正常游戏退出标记

# 按钮
EXIT_BUTTON = 'q'
UP_BUTTON = 'w'
DOWN_BUTTON = 's'
LEFT_BUTTON = 'a'
RIGHT_BUTTON = 'd'




#  GameMsgDict 索引值
ExitGameFlag = 0x0001  # 退出游戏表示
HandleID = 0x0002      # 事件处理句柄
NO_HANDLE = 0          # 空句柄
EventType = 0x0003     # 事件类型
NoneEventType = None   # 空类型
WinnerFlag = 0x0004    # 游戏胜利标识：true 表示回合胜利，false 表示尚未胜利
FalserFlag = 0x0005    # 游戏失败标识：true 表示回合失败，false 表示尚未失败
DataSet = 0x0006       # 数据集索引
BoardArray = 0x0007    # 棋盘索引
Score = 0x0008         # 当前成绩索引
TEST_txt = 0xF001          # 测试数据
xpos = "xpos"
ypos = "ypos"
showtext = "showtext"

class ExitException(Exception):
    pass


class AppRun(object):

    def __init__(self, screen):
        self.GameMsgDict =self._get_init_msg()
        self.screen = screen
        pass

    def _get_empty_board(self):
        return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def _get_init_msg(self):
        return {
            ExitGameFlag :True,      # 默认为游戏退出状态
            HandleID:NO_HANDLE,      # 空句柄
            EventType:NoneEventType, # 空事件
            WinnerFlag:False,        # 回合胜利标识
            FalserFlag:False,        # 回合失败标识
            DataSet:{                # 关键数据集
                BoardArray:self._get_empty_board(),
                Score:0,
                TEST_txt:{xpos:0,ypos:0,showtext:"o"}
            }
        }

    def InitGame(self, gmsg=None):
        """ 初始化游戏
        """
        return True
        pass

    def LoadScr(self, gmsg=None):
        """ 加载资源
        """
        return True
        pass

    def HandleEvents(self,gmsg=None):
        """ 处理事件
        """
        keyvalue = self.screen.getch()
        if keyvalue == ord(EXIT_BUTTON):
            self.ExitGame()
            pass
        else:
            self._move(keyvalue)
            pass
        pass

    def _move(self, towords):
        """
        xpos + > 屏幕向右
        xpos - > 屏幕向左
        ypos + > 屏幕向下
        ypos - > 屏幕向上

        :param towords:
        :return:
        """
        if towords == ord(UP_BUTTON):
            self.GameMsgDict[DataSet][TEST_txt][ypos] -= 1
        elif towords == ord(DOWN_BUTTON):
            self.GameMsgDict[DataSet][TEST_txt][ypos] += 1
        elif towords == ord(RIGHT_BUTTON):
            self.GameMsgDict[DataSet][TEST_txt][xpos] += 1
        elif towords == ord(LEFT_BUTTON):
            self.GameMsgDict[DataSet][TEST_txt][xpos] -= 1
        else:
            pass
        pass


    def UpdateData(self, gmsg=None):
        """ 更新数据
        """
        data_set = self.GameMsgDict[DataSet]
        test_txt = data_set[TEST_txt]
        self.screen.addstr(test_txt[ypos], test_txt[xpos], test_txt[showtext])
        pass


    def RenderDraw(self, gmsg=None):
        """ 渲染/绘图
        """
        self.screen.refresh()
        pass

    def ExitGame(self, exitStatus=None):
        """ 退出游戏
        """
        if  exitStatus is None:
            raise ExitException("Default Exiting.")
        else:
            raise ExitException(exitStatus)
            pass
        pass

    def __call__(self, *args, **kwargs):
        """
        主循环函数
        :param args:
        :param kwargs:
        :return:
        """
        if not self.InitGame():
            self.ExitGame(NOT_INIT_GAME)
        if not self.LoadScr():
            self.ExitGame(NOT_LOAD_SRC)
        self.GameMsgDict = self._get_init_msg()  # 初始化消息字典
        self.GameMsgDict[ExitGameFlag] = False   # 设置游戏开始
        while True:
            self.HandleEvents()
            self.UpdateData()
            self.RenderDraw()
            if self.GameMsgDict[ExitGameFlag]:
                self.ExitGame(ExitGameFlag)
            pass
        pass

    pass

def curses_main(stdscr,msg=None):
    AppObj = AppRun(stdscr)  # 实例化 AppRun
    AppObj()                 # 运行 AppRun 主循环
    pass

if __name__ == "__main__":
    curses.wrapper(curses_main)
    pass
