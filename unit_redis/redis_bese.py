# -*- coding: utf-8 -*-
import redis
import json

def redis_key():
    r = redis.Redis(host='127.0.0.1', port=6379)
    r.set('foo', 'Bar')
    print(r.get('foo'))

    r.set('foo', 'Bar1')
    r.set('foo', 'Bar2')

    print(r.get('foo'))

    r.set('foo1', 'Bar1')
    r.set('foo2', 'Bar2')
    r.set('foo3', 'Bar3')
    abc='string'

    r.set('foo4', abc)

    print(str(r.get('foo1')))
    print(type(r.get('foo2')))
    print(r.get('foo4'))

    data={
        'a1':'a1111',
        'a2':'a2222',
        'a2':'a3333'
    }

    json_str=json.dumps(data)

    r.set('cccccc', json_str)

    re_date= r.get('cccccc')
    print(re_date)
    print(type(re_date))
    u1=re_date.decode('utf-8')
    print(u1)
    print(type(u1))

    guo_01=json.loads(u1)
    print('a1:',guo_01['a1'])

def redis_list():
    r = redis.Redis(host='127.0.0.1', port=6379)

    for i in range(10):
        list_num='http://www.baidu.com/wd=abc%d' % (i)
        r.lpush('list_guo',list_num)

    cmfu1=r.lpop('list_guo')
    cmfu2 = r.lpop('list_guo')

    print('cmfu1:',cmfu1)
    print('cmfu1_type:',type(cmfu1))
    print(cmfu2)
    print(cmfu2.decode('utf-8'))
    print(type(cmfu2.decode('utf-8')))

redis_list()

