# -*- coding: utf-8 -*-
import redis
import json
import requests


def redis_list(data_name,data):
    r = redis.Redis(host='127.0.0.1', port=6379)
    r.lpush(data_name,data)


url='http://oa.9oe.com/index.php/book/api'
html=requests.get(url).text

print(html)
print(type(html))
json_html=json.loads(html)
print(type(json_html))
for item in json_html['data']:
    print(item)
    print(type(item))

    item['model']='qidian_name'
    redis_list('qidian_name',item)

print('end')



