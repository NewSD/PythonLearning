#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: Test.py
@time: 2020/2/20 14:57
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

s = set([1, 2, 3, 4])
print(s)

s = set('spam')
print(s)
s.add('alot')
print(s)

s1 = {1, 2, 3, 4}
print(s1 & {1, 3})
print(s1 | {1, 3, 5, 6})
print(s1 - {1, 3, 4})
print(s1 > {1, 3})

print(type({}))

S = set()
S.add(1.23)
print(S)
# TypeError: unhashable type: 'list'
# s.add([1,2,3])
S.add((1, 2, 3))
print(S)
print(S | {(4, 5, 6), (1, 2, 3)})

print({x ** 2 for x in [1, 2, 3, 4]})

x = {x for x in 'spam'}
print(x)
c4 = {c * 4 for c in 'spam'}
print(c4)
c4 = {c * 4 for c in 'spamham'}
print(c4)
