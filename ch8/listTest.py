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

print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])

print(['Ni!'] * 4)

print(str([1, 2]) + "34")
print([1, 2] + list("34"))

print(3 in [1, 2, 3])

for x in [1, 2, 3]:
    print(x, end=" ")

rec = [c * 4 for c in 'SPAM']
print(rec)
rec = []
for c in 'SPAM':
    rec.append(c * 4)
print(rec)

print(list(map(abs, [-1, -2, 0, 1, 2])))

L = ['spam', 'ham', 'eggs']
print(L[2])
print(L[-2])
print(L[1:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])

L = ['spam', 'Spam', 'SPAM']
L[1] = 'eggs'
print(L[1])
print(L)
L[0:2] = ['eat', 'more']
print(L)
del L[1]
print(L)

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)
L[1:1] = [6, 7]
print(L)
L[1:2] = []
print(L)

L = [1]
L[:0] = [2, 3, 4]
print(L)
L[len(L):] = [5, 6, 7]
print(L)
L.extend([8, 9, 10])
print(L)
L.sort()
print(L)

L = ['eat', 'more', 'SPAM!']
L.append('please')
print(L)
L.sort()
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)
L.sort(key=str.lower)
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)
print(L)

L = ['abcdd', 'ABDss', 'aBeff']
sorted(L, key=str.lower, reverse=True)
print(L)

L = ['abcddsdfa', 'ABDss', 'aBeff']
sorted([x.lower() for x in L], reverse=True)
print(L)