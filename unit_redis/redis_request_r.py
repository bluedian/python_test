# -*- coding: utf-8 -*-
import redis
import json
import requests


def redis_list_read(data_name):
    r = redis.Redis(host='127.0.0.1', port=6379)
    abc = r.lpop(data_name)

    if abc is None:
        print('无数据了')
        exit()

    print(abc)
    print(type(abc))

    abc_dic = abc.decode('utf-8')
    print('abc_dic-->type-->:', type(abc_dic))

    try:
        abc_json = json.loads(abc_dic.replace("'", "\""))
        print(abc_json)
        print(type(abc_json))
        print(abc_json['name'])
    except:
        print('---------')
        print(abc_dic)
        print(type(abc_dic))

    abc_json = json.loads(abc_dic.replace("'", "\""))
    print(abc_json)


redis_list_read('qidian_name')
