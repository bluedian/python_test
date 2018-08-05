# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def getHtml(query_url):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        # conn = requests.session()
        req = requests.get(query_url, headers=header, timeout=5)
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return


def soupHtmlTag(query_url, selectTag, num=0):
    html = getHtml(query_url)
    if html is None:
        print('有问题')

    soup = BeautifulSoup(html, 'html.parser')
    abc = soup.select(selectTag)[num]
    print(abc)


def soupHtml(query_url):
    html = getHtml(query_url)
    if html is None:
        print('有问题')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def fun_model_find(soup, selectTag, isHtml=False):
    '''
    据条件分析网页内容反回数据
    :param soup: BS4类
    :param selectTag: 查找的TAG标记(lmxl)
    :param num: 排行第几个
    :param filter: 过滤字段
    :param isHtml: 是否返回HTML
    :return:
    '''
    try:
        selectlist = selectTag.split('|||')
        infoBook = soup.select(selectlist[0])
        if len(selectlist) > 1:
            num = int(selectlist[1])
            infoBook = infoBook[num]
        if len(selectlist) > 2:
            filter = selectlist[2]
            infoBook = infoBook.get_text()
            infoBook = infoBook.replace(filter, '', 2)
        return infoBook
    except:
        pass
    return


def test():
    url_server = 'http://oa.9oe.com/index.php/book/apiscrapy/work_bookinfo_scrapy'

    req = requests.post(url_server)

    json_data = req.json()

    print(type(json_data))
    print(json_data)
    print('-----')

    if json_data['code'] > 0:
        print(json_data['message'])

    if 'result' in json_data:
        bookinfo = json_data['result']['bookinfo']
        plan = json_data['result']['plan']

        # print(bookinfo)
        # print(plan)
        print(bookinfo['url'])
        planBookupdate = plan['bookupdate']

        scrapy_soup = soupHtml(bookinfo['url'])

        print(fun_model_find(scrapy_soup, plan['bookauthor']))
        print(fun_model_find(scrapy_soup, plan['bookupdate']))

        # print(fun_model_find(scrapy_soup, plan['booklist']))

        scrapy_soup = soupHtml('https://www.biquta.com/14_14718/9033843.html')

        bookcontext = fun_model_find(scrapy_soup, plan['bookcontext'])

        print(len(bookcontext))


url = 'https://www.biquta.com/14_14718/9033843.html'
tag = 'div#content'
num = 0

test()

# soupHtmlTag(url,tag,num)
