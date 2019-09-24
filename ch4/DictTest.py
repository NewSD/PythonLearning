#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: DictTest.py
@time: 2019/9/24 12:44
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

D = {'food': 'Spam', 'quality': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quality'] += 1
print(D)

E = {}
E['name'] = 'Bob'
E['job'] = 'dev'
E['age'] = 40
print(E)
print(E['name'])

bob1 = dict(name='Bob1', job='dev', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob2', 'dev', 39]))
print(bob2)
