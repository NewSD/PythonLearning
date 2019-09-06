#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: ListTest.py
@time: 2019/9/6 16:25
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

L = [123, 'spam', 1.23]
print(L)
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)
print(L)
L.append('NI')
print(L)
print(L.pop(2))
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)
print(M[1])
print(M[1][2])
col2 = [row[1] for row in M]
print(col2)
print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))

print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
