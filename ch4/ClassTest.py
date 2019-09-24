#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: ClassTest.py
@time: 2019/9/24 14:51
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith',50000)
sue = Worker('Sue Jones',60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)