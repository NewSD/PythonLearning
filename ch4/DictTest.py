#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: DictTest.py
@time: 2019/9/24 12:44
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

D = {'food': 'Spam', 'quality': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quality'] += 1
print(D)

E = {}
E['name'] = 'Bob'
E['job'] = 'dev'
E['age'] = 40
print(E)
print(E['name'])

bob1 = dict(name='Bob1', job='dev', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob2', 'dev', 39]))
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 35.5}
print(rec)
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
print(rec['job'][-1])
rec['job'].append('janitor')
print(rec)
rec = 0
print(rec)

D = {'b': 1, 'a': 2, 'c': 3}
print(D)
D['e'] = 99
print(D)
# print(D['f'])
print('f' in D)
if not 'f' in D:
    print('missing')

if not 'f' in D:
    print('missing')
    print('no,really ....')

value = D.get('x', 0)
print(value)

value = D['x'] if 'x' in D else 0
print(value)

Ks = list(D.keys())
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'Spam':
    print(c.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print(squares)
