import math, random

num = 123 + 456
print(num)
num2 = 1.5 * 4
print(num2)
num3 = 2 ** 100
print(num3)
# l = len(str(2**1000000))
# print(l)
a = 3.1415 * 2
print(a)
print(3.1415 * 2)

print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1, 2, 3, 4]))

S = 'Spam'
print(len(S))
print(S[0])
print(S[1])
print(S[-1])
print(S[-2])
print(S[len(S) - 1])
print(S)
print(S[1:3])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[0:-1])
print(S[:])
print(S + 'xyz')
print(S * 8)
# TypeError: 'str' object does not support item assignment
# S[0] = 'z'
S = 'z' + S[1:]
print(S)
S = 'shrubbery'
L = list(S)
print(L)
L[1]='c'
print(''.join(L))
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())