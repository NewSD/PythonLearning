#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: forTest.py
@time: 2019/9/26 14:54
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]

a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1

x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')

x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print(x, end=' ')

for y in range(1,100,2):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y,'has factor ', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


found = False
# while x and not found: