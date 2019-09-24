#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: TypeTest.py
@time: 2019/9/24 18:58
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

A = "spam"
B = A
B = "shrubbery"
print(A)

A = ["spam"]
B = A
B[0] = "shrubbery"
print(A)

A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print(A)

a = 3
b = a
# a = 'spam'
a = a + 2
print(a)
print(b)

L1 = [2, 3, 4]
L2 = L1
print(L1)
print(L2)
L2 = 24
print(L2)

L1 = [2, 3, 4]
L2 = L1
L2[0] = 24
print(L1)
print(L2)

L1 = [2, 3, 4]
L2 = L1[:]
L2[0] = 24
print(L1)
print(L2)

import copy

Y = [1, 2, 4, 5, 6, 7]
X = copy.copy(Y)
print(X)
X = copy.deepcopy(Y)
print(Y)
print(X)

L = [1, 2, 3]
M = L
print(L == M)
print(L is M)

L = [1, 2, 3]
M = [1, 2, 3]
print(L == M)
print(L is M)

X = 42
Y = 42
print(X == Y)
print(X is Y)

import sys
print(sys.getrefcount(1))