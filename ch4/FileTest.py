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

packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('data.bin', 'wb')
file.write(packed)
file.close()

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh', data))

# Unicode

S = 'sp\xc4m'
print(S)
print(S[2])

file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()

text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text))
raw = open('unidata.txt', 'rb').read()
print(raw)
print(raw.decode('utf-8'))

print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(len(text.encode('latin-1')), len(text.encode('utf-16')))

print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))

import codecs

read = codecs.open('unidata.txt', encoding='utf-8').read()
print(read)

rb__read = open('unidata.txt', 'rb').read()
print(rb__read)

txt__read = open('unidata.txt').read()
print(txt__read)