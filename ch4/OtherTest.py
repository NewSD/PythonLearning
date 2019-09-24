#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: OtherTest.py
@time: 2019/9/24 14:23
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

X = set('spam')
print(X)

Y = {'h', 'a', 'm'}
print(Y)

print(X, Y)
Z = X, Y
print(Z)

print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)

print({n ** 2 for n in [1, 2, 3, 4]})

print(list(set([1, 2, 1, 3, 1])))
print(set('spam') - set('ham'))
print(set('spam') == set('asmp'))

print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1 / 3)
print(2 / 3)
print((2 / 3) + (1 / 3))
print((2 / 3) + (1 / 2))

import decimal
d = decimal.Decimal('3.141')
# <class 'decimal.Decimal'>
print(type(d))
print(d+1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction
f = Fraction(2,3)
print(f)
print(f+1)
print(f+Fraction(1,2))

print(1>2, 1<2)
print(bool('spam'))
X = None
print(X)

L = [None] * 100
print(L)

if type(L) == type([]):
    print('yes')
if type(L) == list:
    print('yes')
if isinstance(L,list):
    print('yes')

