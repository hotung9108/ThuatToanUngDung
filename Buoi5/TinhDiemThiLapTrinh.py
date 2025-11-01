from collections import namedtuple

n = int(input())
sv = namedtuple("sv", input() + " S")
A = []
for i in range(n):
    a, b, c, d, e, f = input().split()
    x = sv(a, b, c, d, e, f, 0)
    t = int(x.A) + int(x.B)*2 + int(x.C)*3 + int(x.D)*4 + int(x.E)*5    
    y = x._replace(S=t)
    A.append(y)
A.sort(key = lambda x:x.TEN)
for x in A:
    print(x.TEN, x.S)