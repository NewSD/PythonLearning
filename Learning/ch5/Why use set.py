#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: Why use set.py
@time: 2020/2/20 15:14
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

L = [1, 2, 3, 1, 2, 4, 5]
print(set(L))
L = list(set(L))
print(L)

l = list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa']))
print(l)

set_ = set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6])
print(set_)

print(set('abcdefg') - set('abdghij'))

print(set('spam') - set(['h', 'a', 'm']))

print(set(dir(bytes)) - set(dir(bytearray)))

print(set(dir(bytearray)) - set(dir(bytes)))


L1,L2= [1,2,3,4,5],[2,5,3,4,1]
print(L1 == L2)
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))
print('spam' == 'asmp',set('spam') == set('asmp'),sorted('spam') == sorted('asmp'))

