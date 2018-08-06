# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import json

import bese_crontab
import bese_config
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

        self.urlScrapyWork = bese_config.urlApiScrapy + '/work_bookinfo_scrapy'
        self.urlScrapyWorkUpdate = bese_config.urlApiScrapy + '/work_bookinfo_scrapy'
        self.urlScrapyWorkUpJson = bese_config.urlApiScrapy + '/work_up_json'

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

    def work_bookinfo(self):
        print('第一步,取采集任务')
        # work_json = bese_unitl.unitPostServerData(bese_config.urlApiScrapy + '/work_bookinfo_scrapy','aaa',isReJson=True)
        work_json = bese_unitl.unitPostServerData(self.urlScrapyWork, isReJson=True)

        if work_json is None:
            return
        if work_json['code'] > 0:
            print(work_json['message'])
            return

        print('第二步,采集任务分析执行')
        if 'result' in work_json:
            book_info = work_json['result']['bookinfo']
            book_plan = work_json['result']['plan']
            webstie = book_plan['webstie']
            bookinfo_soup = bese_unitl.unitSoupHtml(book_info['url'])

            if bookinfo_soup in None:
                return

            print('第三步,分析书内容')
            upBookInfo = dict()
            upBookInfo['json'] = 'true'
            upBookInfo['model'] = 'scrapy_updata'
            upBookInfo['scrapy_id'] = book_info['id']

            upBookInfo['scrapy_url'] = book_info['url']
            upBookInfo['bookinfo_title'] = bese_unitl.unitFindTag(bookinfo_soup, 'title')
            upBookInfo['bookinfo_name'] = bese_unitl.unitFindTag(bookinfo_soup, book_plan['bookname'])
            upBookInfo['bookinfo_author'] = bese_unitl.unitFindTag(bookinfo_soup, book_plan['bookauthor'])
            upBookInfo['bookinfo_update'] = bese_unitl.unitFindTag(bookinfo_soup, book_plan['bookupdate'])
            upBookInfo['bookinfo_uptext'] = bese_unitl.unitFindTag(bookinfo_soup, book_plan['bookuptext'])
            upBookInfo['bookinfo_subnum'] = 0
            upBookInfo['bookinfo_sublist'] = []

            print('第四步,分析书章节')
            itmeList = bese_unitl.unitFindTag(bookinfo_soup, book_plan['booklist'], isText=False)
            subList = []
            for itme in itmeList:
                dictData = {
                    'title': itme.text,
                    'url': itme.attrs['href'],
                    'url_all': urljoin(webstie, itme.attrs['href']),
                }
                if dictData in subList:
                    subList.remove(dictData)
                subList.append(dictData)

            upBookInfo['bookinfo_subnum'] = len(subList)
            upBookInfo['bookinfo_sublist'] = subList

            print('第五步,上传数据')
            message = bese_unitl.unitPostServerData(self.urlScrapyWorkUpJson, upBookInfo, isUpJson=True)
            return message




    def run(self):
        '''
        任务运行主函数
        :return:
        '''
        print('run')

        if self.work_bookinfo() is None:
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
