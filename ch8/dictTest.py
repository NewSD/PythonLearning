#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: ami
@license: Apache Licence 
@file: dictTest.py
@time: 2019/9/25 18:26
@tools: PyCharm
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

d = {'name': 'Bob', 'age': 40}
print(d)

d = {'spam': 2, 'ham': 1, 'eggs': 3}
print(d['spam'])
print(d)

print(len(d))
print('ham' in d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

for i in d.items():
    print(i)

d['ham'] = ['grill', 'bake', 'fry']
print(d)

del d['eggs']
print(d)
d['brunch'] = 'Bacon'
print(d)

print(list(d.values()))
print(list(d.keys()))
print(list(d.items()))

print(d.get('ham'))
print(d.get('toast'))
print(d.get('toast', 88))
print(d)
d2 = {'toast': 4, 'muffin': 5}
d.update(d2)
print(d)
print(d.pop('muffin'))
print(d.pop('toast'))
print(d)

table = {
    '1975': 'Holy Grail',
    '1979': 'Life of Brain',
    '1983': 'The Meaning of Life'
}
year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

table2 = {
    'Holy Grail': '1975',
    'Life of Brain': '1979',
    'The Meaning of Life': '1983'
}
print(table2['Holy Grail'])
print(list(table2.items()))

year_ = [title for (title, year) in table2.items() if year == '1975']
print(year_)

K = 'Holy Grail'
print(table2[K])
V = '1975'
key = [key for (key, value) in table2.items() if value == V]
print(key)
key = [key for key in table2.keys() if table2[key] == V]
print(key)
