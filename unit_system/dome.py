# -*- coding: utf-8 -*-

strs='封神大天王最新章节_封神大天王无弹窗全文阅读_顶点小说'
print(strs.index('最新章节'))
if strs.index('最新章节')>1:
    print(strs.index('最新章节'))
    print(strs[:strs.index('最新章节')])

str000='//vip12345'
print(str000.find('vip'))

print('-------------------')
abc=[]
abc.append('a')
abc.append('b')
abc.append('c')
abc.append('d')
abc.append('e')
print(abc)
if 'f' not in abc:
    abc.append('f')
    print('加入一个F')
print(abc)
print('-------------------')

if 'f' not in abc:
    print('--->无F')
else:
    print('--->有F')
print(abc)
print('-------------------')

print('取第一个:',abc.pop(0))
print(abc)


from queue import Queue #LILO队列
q = Queue() #创建队列对象
q.put(0)    #在队列尾部插入元素
q.put(1)
q.put(2)
print('LILO队列',q.queue)  #查看队列中的所有元素
abc_q=q.get()
print(abc_q)  #返回并删除队列头部元素

print(q.queue)
