# -*- coding:utf-8 -*-
import sys
import time

def timecost(func):
    def _wrapper(*args, **kwargs):
        t = time.time()
        ans = func(*args,**kwargs)
        t = time.time() - t
        print("{0} coast {1}s".format(func.__name__,t))
        return ans
        pass
    return _wrapper
    pass



if __name__ == '__main__':

    pass
