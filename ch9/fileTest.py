#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: fileTest.py
@time: 2019/9/26 12:40
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

print(open('myfile.txt').read())

for line in open('myfile.txt'):
    print(line, end='')

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt').read()
print(chars)

F = open('datafile.txt')
line = F.readline()
print(line)
print(line.rstrip())

readline = F.readline()
print(readline)
parts = readline.split(',')
print(parts)

print(int(parts[1]))

numbers = [int(P) for P in parts]
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')
print(parts)
print(eval(parts[0]))
objects = [eval(P) for P in parts]
print(objects)

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle

pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)
print(open('datafile.pkl', 'rb').read())

# Json
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
import json

s = json.dumps(rec)
print(s)
o = json.loads(s)
print(o)
print(o == rec)
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())

P = json.load(open('testjson.txt'))
print(P)

import csv

rdr = csv.reader(open('csvdata.txt'))
for row in rdr: print(row)

F = open('data.bin','wb')
import struct
data = struct.pack('>i4sh',7,b'spam',8)
print(data)
F.write(data)
F.close()

F = open('data.bin','rb')
data = F.read()
values = struct.unpack('>i4sh',data)
print(values)
