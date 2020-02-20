#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: dynamic Type.py
@time: 2020/2/20 15:49
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

a = 3
print(a)
print(type(a))
a = 'spam'
print(type(a))
a = 1.23
print(type(a))

b = a
a = 'spam'
print(type(b))
print(type(a))
b = b + 2
print(b)

