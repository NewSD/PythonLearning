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

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
import math

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sin(0))

print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)

print(abs(-78.0213), sum((1, 2, 3, 4)))
print(min(3, 1, 2, 4), max(3, 2, 1, 4))

print((1 / 3.0))

print(pow(144, .5))
print(math.sqrt(1234567890))
print(1234567890 ** .5)
print(pow(1234567890, .5))

import random

print(random.random())

print(random.randint(1, 10))

print(random.choice(['a', 'b', 'v', 'sdf']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(suits)

from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x)
print(y)
print(Fraction(4, 3))

print(x + y)
print(x - y)
print(x * y)

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

a = 1 / 3.0
b = 4 / 6.0
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3)

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

print(1 / 3)
print(Fraction(1, 3))
print(Decimal(1) / Decimal(3))

print(1 / 3 + 6 / 12)
print(Fraction(1, 3) + Fraction(6, 12))

print(Decimal(str(1 / 3)) + Decimal(str(6 / 12)))

ratio = (2.5).as_integer_ratio()
print(ratio)

