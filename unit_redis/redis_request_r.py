# -*- coding: utf-8 -*-
import redis
import json
import requests


def redis_list_read(data_name):
    r = redis.Redis(host='192.168.1.123', port=6379)
    abc = r.lpop(data_name)
    print(abc)
    print(type(abc))

    abc_dic = abc.decode('utf-8')
    print('abc_dic-->type-->:', type(abc_dic))

    try:
        abc_json = json.loads(abc_dic)
        print(abc_json)
        print(type(abc_json))
        print(abc_json['name'])
    except:
        print('---------')
        print(abc_dic)
        print(type(abc_dic))

    abc_json = json.loads(abc_dic)
    print(abc_json)


redis_list_read('qidian_name')
