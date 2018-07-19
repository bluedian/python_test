# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import time
import json
import re

import bese_crontab
import bese_config


class book_key():

    def __init__(self):
        '''
        初始化
        '''
        self.indexName = 'book_key.py'
        self.version = '0.0.1'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexPathName = self.indexPath + '/' + self.indexName

        self.indexCronComt = 'gsjob_book_key'
        self.indexCronTime = '*/5 * * * *'

        self.urlApiBook = 'http://oa.9oe.com/index.php/book/apibook'
        self.urlFindBaidu = 'https://www.baidu.com/s?wd='

        self.testBookName = '明朝败家子'

    def info(self):
        '''
        显示类的基本信息
        :return:
        '''
        print('indexName:', self.indexName)
        print('version:', self.version)
        print('indexCronTime:', self.indexCronTime)
        print('indexCronComt:', self.indexCronComt)

    def init_cron(self):
        '''
        增加类的时间任务执
        :return:
        '''
        print('init_cron')
        commond = 'python3 ' + self.indexPathName
        comment = self.indexCronComt
        cron = bese_crontab.bese_crontab()
        cron.appendCron(setmin=2, comd=commond, comt=comment)

    def del_cron(self):
        '''
        清理类的所有时间任务
        :return:
        '''
        print('del_cron')
        cron = bese_crontab.bese_crontab()
        cron.delCron(comt=self.indexCronComt)

    def fun_debug(self, funData, strData):
        print('fun____def:', funData)
        print('data_print:', strData)
        print('data__type:', type(strData))

    def fun_getHtml(self, query_url, isReUrl=False):
        try:
            reDate = {}
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            }
            req = requests.get(query_url, headers=header, timeout=2)
            req.encoding = req.apparent_encoding

            reDate['htmlUrl'] = req.url
            reDate['htmltext'] = req.text
            reDate['status_code'] = req.status_code
            reDate['encoding'] = req.encoding

            if isReUrl:
                return reDate
            if req.status_code == 200:
                return reDate['htmltext']
            return
        except:
            return

    def fun_post_api_book(self, upData, isCallJson=True, isDebug=False):
        # print('fun_post_api_book')
        reDate = ''
        req = requests.post(url=self.urlApiBook, data=upData)
        if req.status_code == 200:
            if isCallJson:
                reDate = req.json()
            else:
                reDate = req.text
        print(reDate)
        if isDebug:
            self.fun_debug('get_api_book', reDate)
        return reDate

    def fun_get_book_key(self):
        upData = {
            'model': 'book_key_get',
        }
        getData = self.fun_post_api_book(upData)
        if getData is None:
            return
        # book_key = getData['data']
        # return book_key['book_key']
        return getData['data']['book_key']

    def fun_soup_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        try:
            htmlTitle = soup.title.get_text()
            if htmlTitle is None:
                return
            return htmlTitle
        except:
            return

    def fun_soup_link_all(self, html, book_name):
        reList = []
        soup = BeautifulSoup(html, 'html.parser')
        a_all = soup.find_all('a')
        for item in a_all:
            if self.fun_is_link(item, book_name):
                reList.append({'title': item.get_text(), 'linkUrl': item.attrs['href']})

        return reList

    def fun_is_link(self, subitem, book_name):
        text_lower = subitem.get_text().lower()
        if text_lower.find(book_name) >= 0:
            return True

    def fun_word_one(self, book_name):
        # subLinks=[]
        # indLinks=[]
        query_url = self.urlFindBaidu + book_name
        self.fun_debug('fun_word_one', query_url)

        html = self.fun_getHtml(query_url)
        listLinks = self.fun_soup_link_all(html, book_name=book_name)
        if listLinks is None:
            return
        jobsCount = len(listLinks)
        for item in listLinks:
            jobsCount = jobsCount - 1
            print('顺序为:', str(jobsCount))
            suba_url = item['linkUrl']
            bese_url = urljoin(suba_url, '/')
            time.sleep(1)
            self.fun_work_two(suba_url)
            time.sleep(2)
            self.fun_work_two(bese_url, index=1)

    def fun_work_two(self, query_url, index=0):
        htmlTemp = self.fun_getHtml(query_url, True)
        if htmlTemp is None:
            return
        htmlURL = htmlTemp['htmlUrl']
        htmlTitle = self.fun_soup_title(htmlTemp['htmltext'])

        upData = {
            'model': 'index_url',
            'index': index,
            'name': htmlURL,
            'title': htmlTitle
        }
        self.fun_post_api_book(upData, isCallJson=False)

    def run(self):
        self.testBookName = self.fun_get_book_key()
        self.fun_word_one(self.testBookName)


if __name__ == '__main__':
    gs_class_self = book_key()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            gs_class_self.init_cron()
        if sys.argv[1] == 'info':
            gs_class_self.info()
        if sys.argv[1] == 'del':
            gs_class_self.del_cron()
    else:
        gs_class_self.run()
