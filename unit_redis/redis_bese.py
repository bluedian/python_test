# -*- coding: utf-8 -*-
import redis

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