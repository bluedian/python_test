# -*- coding: utf-8 -*-
import test1

class test4(object):
    def __init__(self):
        pass

    def tt(self):
        t1=test1.test1()
        t1.pp()


if __name__ == '__main__':
    print('正确调用同级类')
    test4().tt()