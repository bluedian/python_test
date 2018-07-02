# -*- coding: utf-8 -*-
import redis
import json

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