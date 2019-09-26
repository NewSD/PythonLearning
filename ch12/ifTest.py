#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: ifTest.py
@time: 2019/9/26 14:43
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

if 1:
    print(True)
else:
    print(False)

if not 1:
    print('true')
else:
    print('false')

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))

choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print("Bad choice")

try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x * 2
    print(x)


