# -*- coding:utf-8 -*-


class ExitException(Exception):
    pass


class AppRun(object):

    def __init__(self):
        pass

    def InitGame(self, gmsg=None):
        """ 初始化游戏
        """
        pass

    def LoadScr(self, gmsg=None):
        """ 加载资源
        """
        pass

    def HandleEvents(self,gmsg=None):
        """ 处理事件
        """
        pass

    def UpdateData(self, gmsg=None):
        """ 更新数据
        """
        pass

    def RenderDraw(self, gmsg=None):
        """ 渲染/绘图
        """
        pass

    def ExitGame(self, exitStatus=None):
        """ 退出游戏
        """
        if isinstance(exitStatus, NoneType):
            raise ExitException("Default Exiting.")
        else:
            pass
        pass

    pass


if __name__ == "__main__":
    pass
