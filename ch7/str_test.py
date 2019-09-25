#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: str_test.py
@time: 2019/9/24 20:46
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

s = '\a'
print(s)

S = ''
S = "spam's"
# S = 's\np\ta\x00m'
# S = """......multiline...."""
print(S.find('pa'))

s = 'a\nb\tc'
print(s)
print(len(s))

x = 'c:\py\code'
print(x)
print(len(x))

myjob = 'hacker'
for c in myjob: print(c, end=' ')
s = 'spam'
print(s[0], s[-2])

s = 'abcdefghijklmnopq'
print(s[1:10:2])
print(s[::2])

s = 'hello'
print(s[::-1])
print(s[3:1:-1])

print(str(3.1415), float(5))

print(ord('s'))
print(chr(115))

print('This is %d %s bird!' % (1, 'dead'))
print('This is {0} {1} bird!'.format(1, 'dead'))

S = 'spammy'
L = list(S)
print(L)
print('9'.join(L))

line = 'aaa bbb ccc'
print(line.split())

line = 'bob,hacker,40'
print(line.split(','))

reply = """
Greeting...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 20}
print(reply % values)
# print(reply.format(values))

template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))

template = '%(motto)s , %(pork)s and %(food)s '
print(template % dict(motto='spam', pork='ham', food='eggs'))
print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))
