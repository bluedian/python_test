# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import redis


def getHtml(query_url):
    display = Display(visible=0, size=(800, 600))
    display.start()
    try:
        driver = webdriver.Firefox()
    except:
        driver = webdriver.Chrome()
    driver.get(query_url)
    print(driver.title)
    html = driver.page_source
    driver.quit()
    display.stop()
    try:
        redis_write(driver.title,query_url)
    except:
        pass
    return html

def redis_write(key_name,key_value):
    r = redis.Redis(host='127.0.0.1', port=6379)
    print(key_name,key_value)
    r.set(key_name,key_value)


def soup_links(query_url):
    html=getHtml(query_url)
    if html is None:
        print('没有取到网页')
        exit()
    soup = BeautifulSoup(html, 'html.parser')
    #links_list = soup.find_all('a',attrs={'href'})
    links_list = soup.find_all('a')
    for item in links_list:
        print(item)



soup_links('http://www.163.com')