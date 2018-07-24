# -*- coding: utf-8 -*-

lista = ['a', 'b', 'c', 'd', 'e']

print(lista)
lista.pop()

print(lista)

li = [1, 2, 6, 3, 4, 6, 5, 1, 2, 3]
new_li = list(set(li))
new_li.sort(key=li.index)
print(new_li)
new_li.sort()
print(new_li)
