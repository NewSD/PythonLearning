#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: tupleTest.py
@time: 2019/9/26 11:53
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

t = (1, 2)
print(t)

print(t + (3, 4))

print((1, 2) * 4)

t = (1, 2, 3, 4)
print(t[0])
print(t[1:3])

x = (40)
print(x)
x = (40,)
print(x)

t = ('cc', 'aa', 'dd', 'bb')
tmp = list(t)
print(tmp)
tmp.sort()
print(tmp)
print(tuple(tmp))
print(sorted(t))

t = (1, 2, 3, 4, 5)
l = [x + 20 for x in t]
print(l)

t = (1, 2, 3, 2, 4, 2)
print(t.index(2))
print(t.index(2, 2))
print(t.count(2))

t = (1, [2, 3], 4)
print(t[1])
# t[1]='spam'
t[1][0] = 'spam'
print(t)

bob = ('bob', 49, ['dev', 'mgr'])
print(bob)
print(bob[0])
print(bob[2])

bob = dict(name='Bob', age=49, jobs=['dev', 'mgr'])
print(bob)
print(bob['name'], bob['jobs'])
print(tuple(bob.values()))
print(list(bob.items()))

from collections import namedtuple

rec = namedtuple('rec', ['name', 'age', 'jobs'])
bob = rec('Bob', age=45, jobs=['dev', 'mgr'])
print(bob)
print(bob[0], bob[2])
print(bob.name, bob.jobs)

o = bob._asdict()
print(o)

