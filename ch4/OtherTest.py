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

print({n ** 2 for n in [1,2,3,4]})

print(list(set([1,2,1,3,1])))
print(set('spam') - set('ham'))
print(set('spam') == set('asmp'))
