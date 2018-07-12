# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

url='http://www.163.com'

def getHtml(query_url):
    req=requests.get(query_url)
    req.encoding=req.apparent_encoding
    html=req.text
    return html


def soupList(query_url):
    html=getHtml(url)
    soup=BeautifulSoup(html,'html.parser')

    links= soup.find_all('a',attrs={'href':re.compile("^http://money")})

    for itme in links:
        print(itme)


print(soupList(url))