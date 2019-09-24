#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: NumTest.py
@time: 2019/9/24 16:52
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
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 ** b)

print(b / 2 + a)
print(b / (2.0 + a))
print(1 / 2.0)

num = 1 / 3.0
print(num)
print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))

print(repr('spam'))
print(str('spam'))

print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)
