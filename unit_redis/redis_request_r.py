# -*- coding: utf-8 -*-
import redis
import json
import requests


def redis_list_read(data_name):
    r = redis.Redis(host='127.0.0.1', port=6379)
    abc=r.lpop(data_name)
    print(abc)
    print(type(abc))
    print(abc.decode('utf-8'))



redis_list_read('qidian_name')
