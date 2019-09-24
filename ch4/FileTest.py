#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: FileTest.py
@time: 2019/9/24 13:54
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

f = open('data.txt', 'w')
f.write('Hello\n')
f.write('hello\n')
f.close()

f = open('data.txt')
text = f.read()
print(text)
print(text.split())

for line in open('data.txt'): print(line)

print(dir(f))
print(help(f.seek))



import struct
packed = struct.pack('>i4sh',7,b'spam',8)
print(packed)

file = open('data.bin','wb')
file.write(packed)
file.close()
