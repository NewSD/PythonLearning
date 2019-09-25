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

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2
Y = 3
Z = 4
z_ = Matrix[(X, Y, Z)]
print(z_)
print(Matrix)

if (2, 3, 6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

print(Matrix.get((2, 3, 4), 0))
print(Matrix.get((2, 3, 6), 0))

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])

rec = {
    'name': 'Bob',
    'jobs': ['developer', 'manager'],
    'web': 'www.bobs.org/?Bob',
    'home': {'state': 'Overworked', 'zip': 12345}
}
print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])
db = []
other = {
    'name': 'other',
    'jobs': ['hr', 'manager'],
    'web': 'www.hr.org',
    'home': {'state': 'Overworked', 'zip': 55555}
}
db.append(rec)
db.append(other)
print(db[0]['jobs'])

db = {}
db['bob'] = rec
db['sue'] = other
db['bob']['jobs']

age_ = {'name': 'Bob', 'age': 40}
print(age_)

d = {}
d['name'] = 'sue'
d['age'] = 50
print(d)

di = dict(name='Bob', age=56)
print(di)

di = dict([('name', 'Bob'), ('age', 55)])
print(di)

fromkeys = dict.fromkeys(['a', 'b'], 0)
print(fromkeys)

iterator = zip(['a', 'b', 'c'], [1, 2, 3])
print(iterator)
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)

d = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(d)

d = {x: x ** 2 for x in [1, 2, 3, 4]}
print(d)
d2 = {x: x ** 2 for x in range(4)}
print(d2)

d = {c: c * 4 for c in 'SPAM'}
print(d)

d = {c.lower(): c + '!' for c in ['spam', 'eggs', 'ham']}
print(d)

d = dict.fromkeys(['a', 'b', 'c'], 0)
print(d)

d = {k: 0 for k in ['a', 'b', 'c']}
print(d)

d = dict.fromkeys('spam')
print(d)
d = dict.fromkeys('spam', 0)
print(d)

d = {k: None for k in 'spam'}
print(d)