# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

import bese_crontab

import requests
from bs4 import BeautifulSoup


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
        self.bookUrl = 'https://www.biquta.com/1_1102/'

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

    def fun_get_html(self, query_url, isReUrl=False):
        try:
            reDate = {}
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            }
            conn = requests.session()
            req = conn.get(query_url, headers=header, timeout=2)
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

    def fun_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def fun_soup_title(self, soup):
        try:
            htmlTitle = soup.title.get_text()
            if htmlTitle is None:
                return
            return htmlTitle
        except:
            return

    def fun_soup_list(self, soup):
        sublist = []
        bookListabc = soup.find_all('dd')

        for item in bookListabc:
            # print(item.a)
            if 'href' in item.a.attrs:
                sublist.append({'title': item.a.text, 'url': item.a.attrs['href']})
                # sublist.append(item.a)
                # sublist.append((item.a.text,item.a.attrs['href']))

        print(sublist)
        print(len(sublist))
        # sublist = list(set(sublist))
        # sublist.sort()
        print(len(sublist))
        for item in sublist:
            print(item)

    def run(self):
        '''
        任务运行主函数
        :return:
        '''
        print('run')
        run_url = self.bookUrl
        run_html = self.fun_get_html(run_url)
        if run_html is None:
            print('无网页')
            return
        # print(run_html)
        run_soup = self.fun_soup(run_html)
        if run_soup is None:
            print('soup 无对象')
            return

        self.fun_soup_list(run_soup)

        pass


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
