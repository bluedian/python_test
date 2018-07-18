# -*- coding: utf-8 -*-
import sys
sys.path.append('')
sys.path.append('..')
sys.path.append('..//test')
print(sys.path)

from test.test1 import test1
#import test.test1

class test2(object):
    def __init__(self):
        pass

    def tt(self):
        t1=test1()
        t1.pp()


if __name__ == '__main__':
    test2().tt()