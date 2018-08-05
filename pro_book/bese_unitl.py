# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def unitGetHtml(query_url):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        req = requests.get(query_url, headers=header, timeout=5)
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return


def unitSoupHtml(query_url):
    html = unitGetHtml(query_url)
    if html is None:
        return
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def unitFindTag(soup, selectTag):
    '''
    据条件分析网页内容反回数据
    :param soup: BS4类
    :param selectTag: 查找的TAG标记(lmxl)
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
