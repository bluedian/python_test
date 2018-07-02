# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))

r.set('foo', 'Bar1')
r.set('foo', 'Bar2')

print(r.get('foo'))