# -*- coding: utf-8 -*-
import os


beseURL = 'http://oa.9oe.com/index.php/book'

url_server_status = beseURL + '/apiserver'

def getPathAll():
    print(os.getcwd())
    print(os.path.abspath(os.path.dirname(__file__)))
    print('***获取上级目录***')
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


getPathAll()