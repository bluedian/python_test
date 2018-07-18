# -*- coding: utf-8 -*-
from test.test1 import test1

class test5(object):
    def __init__(self):
        pass

    def tt(self):
        t1=test1.test1()
        t1.pp()


if __name__ == '__main__':
    test5().tt()