# -*- coding: utf-8 -*-
import os, sys
sys.path.append('..')
from bs4 import BeautifulSoup
import requests

import bese_crontab
import bese_unitl

class pro_scrapy_books():
    '''
    工程使用模板
    '''
    def __init__(self):
        '''
        初始化
        '''
        self.indexName = 'pro_scrapy_books.py'
        self.version = '0.0.1'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexPathName = self.indexPath + '/' + self.indexName

        self.indexCronComt = 'gsjob_pro_scrapy_books'
        self.indexCronTime = '*/2 * * * *'

    def info(self):
        '''
        显示类的基本信息
        :return:
        '''
        print('indexName:', self.indexName)
        print('version:', self.version)
        print('indexCronTime:', self.indexCronTime)
        print('indexCronComt:', self.indexCronComt)

    def init_cron(self, setM=2):
        '''
        增加类的时间任务执
        :return:
        '''
        print('init_cron')
        commond = 'python3 ' + self.indexPathName
        comment = self.indexCronComt
        cron = bese_crontab.bese_crontab()
        cron.appendCron(setmin=setM, comd=commond, comt=comment)

    def del_cron(self):
        '''
        清理类的所有时间任务
        :return:
        '''
        print('del_cron')
        cron = bese_crontab.bese_crontab()
        cron.delCron(comt=self.indexCronComt)

    def run(self):
        '''
        任务运行主函数
        :return:
        '''
        print('run')

        print(bese_unitl.unitGetHtml('http://www.163.com'))
        pass


if __name__ == '__main__':
    gs_class_self = pro_scrapy_books()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            gs_class_self.init_cron()
        if sys.argv[1] == 'info':
            gs_class_self.info()
        if sys.argv[1] == 'del':
            gs_class_self.del_cron()
    else:
        gs_class_self.run()
