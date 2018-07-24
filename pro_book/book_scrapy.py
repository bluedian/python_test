# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

import bese_crontab

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
from lxml import etree


class book_scrapy():
    '''
    工程使用模板
    '''

    def __init__(self):
        '''
        初始化
        '''
        self.indexName = 'book_scrapy.py'
        self.version = '0.0.1'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexPathName = self.indexPath + '/' + self.indexName

        self.indexCronComt = 'gsjob_book_scrapy'
        self.indexCronTime = '*/2 * * * *'
        # test
        self.workUrl = 'http://oa.9oe.com/index.php/book/apibook'
        self.bookUrl = 'https://www.biquta.com/1_1102/'
        self.rootUrl = ''

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

    def fun_work_url(self, data, query_url=None, isJson=False):
        if query_url is None:
            query_url = self.workUrl
        if isJson:
            req = requests.post(query_url, json=json.dumps(data))
            return req.text
        else:
            req = requests.post(query_url, data=data)
            abc = req.json()
            if 'success' in abc:
                return abc

    def fun_work_test(self, data):
        # scrapy_test_url = 'http://www.123.com/index.php/book/apibook/reshow'
        scrapy_test_url = 'http://oa.9oe.com/index.php/book/apibook/reshow'
        if 'json' in data:
            return self.fun_work_url(data, query_url=scrapy_test_url, isJson=True)
        return self.fun_work_url(data, query_url=scrapy_test_url)

    def fun_get_html(self, query_url, isReUrl=False):
        try:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            }
            # conn = requests.session()
            req = requests.get(query_url, headers=header, timeout=5)
            req.encoding = req.apparent_encoding

            reDate = dict()
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

    def fun_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def fun_soup_title(self, soup):
        if soup is None:
            return
        return soup.title.get_text()

    def fun_model_book_info(self, soup, selectTag, num=999, isHtml=False):
        try:
            if num == 999:
                infoBook = soup.select(selectTag)
                print(infoBook)
            else:
                infoBook = soup.select(selectTag)[num]
            if infoBook:
                if isHtml:
                    return infoBook
                return infoBook.get_text()
        except:
            pass
        return

    def fun_model_book_list(self, soup, selectTag):
        sublist = []
        bookList = soup.select(selectTag)

        for item in bookList:
            dictData = {
                'title': item.text,
                'url': item.attrs['href'],
                'url_all': self.url_join(item.attrs['href']),
            }
            if dictData in sublist:
                sublist.remove(dictData)
            sublist.append(dictData)
        return sublist

    def url_join(self, pathUrl):
        return urljoin(self.rootUrl, pathUrl)

    def work_job_get(self):
        data = {'aaa': 'aaa'}
        work = self.fun_work_url(data)
        # print(work)
        # print(work['scrapyurl'])
        return work['scrapyurl']

    def work_job_update(self, bookInfo):
        bookInfo['model'] = 'scrapy_job_update'
        work = self.fun_work_url(bookInfo)

    def run_test(self):
        bookInfo = dict()
        bookInfo['json'] = 'true'
        bookInfo['scrapy_url'] = 'scrapy_url'
        bookInfo['info_book_title'] = 'info_book_title'
        bookInfo['info_book_name'] = 'info_book_name'
        bookInfo['info_book_author'] = 'info_book_author'
        bookInfo['info_book_update'] = 'info_book_update'
        bookInfo['info_book_uptext'] = 'info_book_uptext'

        print(self.fun_work_test(bookInfo))

    def run_job(self):

        '''
        任务运行主函数
        :return:
        '''
        print('run')
        print('第一步,取采集地址(网络取)')
        runUrl = self.work_job_get()

        print('第二步,分析主域名,分析网页')
        self.rootUrl = urljoin(runUrl, '\\')
        runHtml = self.fun_get_html(runUrl)

        if runHtml is None:
            print('无网页')
            return

        runSoup = self.fun_soup(runHtml)
        if runSoup is None:
            print('soup 无对象')
            return

        print('第三步,分析书内容')
        bookInfo = dict()
        bookInfo['json'] = 'true'
        bookInfo['scrapy_url'] = runUrl
        bookInfo['info_book_title'] = self.fun_soup_title(runSoup)
        bookInfo['info_book_name'] = self.fun_model_book_info(runSoup, 'div#info > h1', 0)
        bookInfo['info_book_author'] = self.fun_model_book_info(runSoup, 'div#info > p', 0)
        bookInfo['info_book_update'] = self.fun_model_book_info(runSoup, 'div#info > p', 2)
        bookInfo['info_book_uptext'] = self.fun_model_book_info(runSoup, 'div#info > p:(4) > a ', 0)
        bookInfo['info_book_subnum'] = 0
        bookInfo['info_book_sublist'] = []

        # print(bookInfo)
        # print(self.fun_work_test(bookInfo))

        print('第四步,分析书章节')
        subList = self.fun_model_book_list(runSoup, 'dd > a[href]')

        # for sub in subList:
        #    print(sub)

        bookInfo['info_book_subnum'] = len(subList)
        bookInfo['info_book_sublist'] = subList

        print('第五步,上传数据.测试上传')
        # print(bookInfo)
        print(self.fun_work_test(bookInfo))

        exit()

    def run(self):
        '''
        任务运行主函数
        :return:
        '''
        for i in range(1):
            self.run_job()


if __name__ == '__main__':
    gs_class_self = book_scrapy()
    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            gs_class_self.init_cron()
        if sys.argv[1] == 'info':
            gs_class_self.info()
        if sys.argv[1] == 'del':
            gs_class_self.del_cron()
    else:
        gs_class_self.run()
        #gs_class_self.run_test()
