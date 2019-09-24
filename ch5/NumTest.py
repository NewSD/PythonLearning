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

X = 2
Y = 4
Z = 6

print(X < Y < Z)
print(X < Y and Y < Z)
print(X < Y > Z)
print(1.1 + 2.2)
print(1.1 + 2.2 == 3.3)
print(int(1.1 + 2.2) == int(3.3))

# from __future__ import division

# print(10 / 4)
# print(10 / 4.0)
# print(10 // 4)
# print(10 // 4.0)

import math

floor = math.floor(2.5)
print(floor)
a = math.floor(-2.5)
print(a)
b = math.trunc(2.5)
print(b)
c = math.trunc(-2.5)
print(c)

print(5 / 2, 5 / -2)
# 1606938044258990275541962092341162602522202993782792835301376
# print(2 ** 200)

print(2 - 3j)
print(1j * 1j)
print(2 + 1j * 3)
print((2 + 1j) * 3)

# 8进制
print(0o1, 0o20, 0o377)
# 16进制
print(0x01, 0x10, 0xff)
# 2进制
print(0b1, 0b10000, 0b11111111)

print(oct(64), hex(64), bin(64))

print(64, 0o100, 0x40, 0b1000000)

print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))

print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))

num = 0xfffffffffff5658ffffff
print(num)
print(oct(num))
print(bin(num))

print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
