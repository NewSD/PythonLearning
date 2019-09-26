#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: expressionTest.py
@time: 2019/9/26 14:15
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)

a, *b = seq
print(a)
print(b)

*a, b = seq
print(a, b)
a, *b, c = seq
print(a, b, c)
a, b, *c = seq
print(a, b, c)

a, *b = 'spam'
print(a, b)
a, *b, c = 'spam'
print(a, b, c)

a, *b, c = range(4)
print(a, b, c)

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

a, b, c, *d = seq
print(a, b, c, d)

a, b, c, d, *e = seq
print(a, b, c, d, e)

a = b = 0
b = b + 1
print(a, b)

a = b = []
b.append(42)
print(a,b)
a = []
b = []
b.append(23)
print(a,b)

s = 'spam'
s += 'SPAM'
print(s)

