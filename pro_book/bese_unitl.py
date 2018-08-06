# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json


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


def unitPostServer(query_url, isJson=True):
    try:
        req = requests.post(query_url)
        req.encoding = req.apparent_encoding
        if isJson:
            return req.json()
        return req.text
    except:
        return


def unitPostServerData(query_url, data=None, isUpJson=False, isReJson=False):
    req = None
    if isUpJson:
        req = requests.post(query_url, json=json.dumps(data))
    else:
        req = requests.post(query_url, data=data)

    req.encoding = req.apparent_encoding
    if isReJson:
        return req.json()
    return req.text


def unitSoupHtml(query_url):
    html = unitGetHtml(query_url)
    if html is None:
        return
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def unitFindTag(soup, selectTag, isText=True):
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
        if isText:
            infoBook = infoBook.get_text()

        if len(selectlist) > 2:
            filter = selectlist[2]
            infoBook = infoBook.replace(filter, '', 2)

        return infoBook
    except:
        pass
    return


def unitHtmlTag(query_url, selectTag):
    '''
    据条件分析网页内容反回数据
    :param soup: BS4类
    :param selectTag: 查找的TAG标记(lmxl)
    :return:
    '''
    soup = unitSoupHtml(query_url)
    if soup is None:
        return
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
