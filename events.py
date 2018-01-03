# -*- coding:utf-8 -*-

class UserInputError(Exception):
    pass

class TryApp(object):
    def __init__(self, name = None):
        self.name = name if name else "bug320"
        pass

    def pname(self):
        print self.name
        pass
    pass


class UserInut(object):
    def __init__(self,functable):
        self.functable = functable
        pass

    def doFunc(self,index):
        func,argv = self.functable[index]
        func(argv)
        pass

    def changeArgs(self, index, args):
        if not index:
            raise
            pass
        func_,args_ = self.functable[index]
        args_ = args
        self.functable(func_,args_)
        pass



    pass

if __name__ == '__main__':
    app = TryApp()
    func = {'p':(app.pname,None)}
    while True:
        a = raw_input("Input:")
        if a == 'q':
            raise UserInputError("InputError")
            break

        pass