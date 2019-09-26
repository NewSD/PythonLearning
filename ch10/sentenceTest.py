#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: sentenceTest.py
@time: 2019/9/26 13:39
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

x = 1
y = 2
if x > y:
    print('x>y')
else:
    print('x<=y')


a = 1; b = 2; print(a + b)

# while True:
#     reply = input("Enter text:")
#     if reply == 'stop': break
#     print(reply.upper())


# while True:
#     reply = input("Enter text:")
#     if reply == 'stop': break
#     print(int(reply)**2)
# print('Bye')



while True:
    reply = input("Enter text:")
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print("Bad!"*8)
    else:
        print(int(reply) ** 2)
print('Bye')