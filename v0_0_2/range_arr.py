# -*- coding:utf-8 -*-
"""
:author bug320
:purpose 2048基本运算
:time 2017-08-18
"""

import random
from os import system
import pygmae

LEN_ARR = 4 # 数组行数
ZERO = 0 # 数组初始值

TWO = 2  # 随机出现的数字2
FOUR = 4 # 随机出现的数字4
RANG_MAX = 99 # 随机上限
RANG_MIN = 0  # 随机下限
LT_TWO = 90   # 出现2的上限

UP = 'A'      # 向上
DOWN = 'B'    # 向下
LEFT = 'D'    # 向左
RIGHT = 'C'   # 向右

def towards_trans(towards):
    ups = ['w','8']
    downs = ['s','2']
    rights = ['d','6']
    lefts = ['a','4']
    if pygame:
        # todo 映射键盘
        pass
    if towards in ups:
        return UP
    if towards in downs:
        return DOWN
    if towards in rights:
        return RIGHT
    if towards in lefts:
        return LEFT
    return -1
    pass

def range_num():
    """
    :return 随机出现一个数
    """
    return TWO if random.randint(RANG_MIN ,RANG_MAX ) < LT_TWO  else FOUR
    pass


def range_poniter(arr):
    """
    :return 出租pointer 里面随机返回一个值为 ZERO 的点的坐标(x,y),如果找不到返回 None
    """
    # 1. 首先把所有值为 ZERO 的点的坐标以元组(x,y)形式放到 数组 tmp 里面
    # 2. 从 随机获取一个比 len(tmp) 小的数 id,返回 tmp[ip]

    tmp = [(i,j) for i in xrange(LEN_ARR) for j in xrange(LEN_ARR) if arr[i][j] == 0 ]

    if not tmp:
        return (-1,-1)

    id  = random.randint(0,len(tmp)-1)
    return tmp[id]
    pass


class Array(object):
    """
    矩阵：移动合并，计算二维矩阵
    """
    def __init__(self, size):
        self.size = size 
        self.arr =[[ ZERO for i in xrange(self.size)] for j in xrange(self.size)]
        # 生成一个r空的二维数组
        pass


    def init(self):
        self.arr =[[ ZERO for i in xrange(self.size)] for j in xrange(self.size)]
        for i in xrange(2):
            self.set_point()
        pass
    def set_point(self):
        x,y = range_poniter(self.arr)
        if x== -1:
            return
        self.arr[x][y] = range_num()
        pass

    def show(self):
        system("cls")
        for tr in self.arr:
            for td in tr:
                print td,
                pass
            print
            pass
        pass
    def has_zero(self, tr):
        for td in tr:
            if td == ZERO:
                return True
        return False
        pass
    def has_nozero(self,tr):
        for td in tr:
            if td != ZERO:
                return True
        return False


    def move_zero(self,trs):
        """
        如果首尾是 ZERO ,就把数组后边的所有值前移一位，末位补 ZERO
        :return
        """
        tr = [td for td in trs]
        if tr[0] == ZERO:
            tr[:-1] = tr[1:]
            tr[-1]  = ZERO
        return tr
        pass

    def is_eq_tr(self,t1,t2):
        for k,v in zip(t1,t2):
            if k != v:
                return False
        return True
        pass
    def move_tr(self, tr):
        """
        把 tr 的 ZERO 都去掉，并把数组前移，空位补 ZERO
        :return
        """
        trs = [td for td in tr]
        for i in xrange(self.size):
            for td in tr:
                if tr[i] == ZERO:
                    if self.has_nozero(tr[i:]):
                        tmp = self.move_zero(tr[i:])
                        tr[i:] = tmp

        if not self.is_eq_tr(tr,trs):
            self.is_move = True
        #for i in xrange(LEN_ARR):
        #    #self.move_zero(tr)
        #    if tr[i] == ZERO:
        #        if self.has_nozero(tr[i:]):
        #            self.is_move = True
        #        tr[i:] = self.move_zero(tr[i:])
        pass

    def add_same(self, tr):
        """
        把 tr 中 相等的连续的2项相加，和放到前一个，后一个置 ZERO
        最后把所有的 ZERO 位移动到尾部，其他按原顺序前移
        :return
        """
        trs = [td for td in tr]
        # 先把 ZERO 都移动到 尾部
        self.move_tr(tr)
        # 计算 和
        for i in xrange(LEN_ARR - 1):
            if tr[i] == ZERO:
                continue
            if tr[i] == tr[i+1]:
                tr[i] *= 2
                tr[i+1] = 0
                self.is_move = True
        # 把求和后的数组 ZERO后移
        is_move = self.is_move
        self.move_tr(tr)
        self.is_move = is_move
        if not self.is_eq_tr(trs,tr):
            self.is_move = True
        return True
        pass
    def add_move(self,tmp):
        mov_ids = []
        for x in xrange(self.size):
            if self.has_nozero(tmp[x]):
                mov_ids.append(x)
                pass
        for id in xrange(self.size):
            self.add_same(tmp[id])
        pass
    def move(self, towards):
        self.is_move = False
        if towards == UP:
            # 向上移动,把 [0,1,2,3]
            tmp = map(list,zip(*self.arr)) # 把数组转置
            self.add_move(tmp)
            self.arr = map(list,zip(*tmp))
            return 
            pass
        if towards == DOWN:
            tmp = map(list,zip(*self.arr))
            tmp = map(lambda tr:tr[::-1],tmp)
            self.add_move(tmp)
            self.arr = map(lambda tr:tr[::-1],tmp)
            self.arr = map(list,zip(*self.arr))
            return 
            pass
        if towards == LEFT:
            tmp = self.arr
            self.add_move(tmp)
            self.arr = tmp
            return 
            pass
        if towards == RIGHT:
            tmp = map(lambda tr:tr[::-1],self.arr)
            self.add_move(tmp)
            self.arr = map(lambda tr:tr[::-1],tmp)
            return 
            pass
        pass
    
    def move_gui(self, towards):
        self.is_move = False
        if towards == UP:
            # 向上移动,把 [0,1,2,3]
            tmp = map(list,zip(*self.arr)) # 把数组转置
            self.add_move(tmp)
            self.arr = map(list,zip(*tmp))
            return 
            pass
        if towards == DOWN:
            tmp = map(list,zip(*self.arr))
            tmp = map(lambda tr:tr[::-1],tmp)
            self.add_move(tmp)
            self.arr = map(lambda tr:tr[::-1],tmp)
            self.arr = map(list,zip(*self.arr))
            return 
            pass
        if towards == LEFT:
            tmp = self.arr
            self.add_move(tmp)
            self.arr = tmp
            return 
            pass
        if towards == RIGHT:
            tmp = map(lambda tr:tr[::-1],self.arr)
            self.add_move(tmp)
            self.arr = map(lambda tr:tr[::-1],tmp)
            return 
            pass
        pass

    def move_put(self,towards):
        towards = towards_trans(towards)
        if towards == -1:
            return
        self.move(towards)
        if self.is_move:
            self.set_point()
        pass

    pass



if __name__ == "__main__":

    # 目的：测试随机数
    #
    # for i in xrange(100):
    #     print range_num(),
    #     if (i+1) % 10 == 0:
    #         print
    #

    # 随机非0位置
    # range_poniter(BASE_ARR)

    # 测试初始化
    a =  Array(LEN_ARR)
    a.init()
    a.show()
    while True:
        towards = raw_input("请输入方向")
        a.move_put(towards)
        a.show()
    pass
