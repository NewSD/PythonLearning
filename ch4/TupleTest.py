#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: TupleTest.py
@time: 2019/9/24 13:48
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

T = (1, 2, 3, 4)
print(len(T))

print(T + (5, 6))
print(T[0])

print(T.index(4))
print(T.count(4))

T = (2,) + T[1:]
print(T)

T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])
