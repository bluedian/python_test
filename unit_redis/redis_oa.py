# -*- coding: utf-8 -*-

import requests
import json


url1='http://oa.9oe.com/index.php/book/apiredis/redis_list_lPush_post'
url2='http://oa.9oe.com/index.php/book/apiredis/redis_list_rpop'
url3='http://oa.9oe.com/index.php/book/apiredis/redis_list_test1111'
url4='http://oa.9oe.com/index.php/book/apiredis/redis_list_test1111/param/param1'

data={
    'model':'12344',
    'aaa':'sssss',
    'url':'http://edu.163.com/18/0712/06/DMGA8EHC00297VGM.html'
}

def htmlPost():
    headers = {'Content-Type': 'application/json'}  ## headers中添加上content-type这个参数，指定为json格式
    req = requests.post(url1, headers=headers, data=json.dumps(data))  ## post的时候，
    #req=requests.post(url1,json=json.dumps(data))
    print(req.text)

def htmlUrlPost(url):
    headers = {'Content-Type': 'application/json'}  ## headers中添加上content-type这个参数，指定为json格式
    req = requests.post(url, headers=headers, data=json.dumps(data))  ## post的时候，
    #req=requests.post(url1,json=json.dumps(data))
    print(req.text)

def htmlGet():
    req = requests.get(url2)
    print()
    html=req.text
    print(html)
    try:
        jsonstr=json.loads(html)
        print('aaa:',type(jsonstr))

        print(jsonstr['url'])
    except:
        print((html))



htmlPost()
print('-----------------')
htmlGet()

htmlUrlPost(url4)


