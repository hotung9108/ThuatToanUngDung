import itertools
x = [3,5,3,2,52,43, 4, "abc", [3, 4, 5], 3]
print(x)
print(*x, sep= " va ", end = " xong ")
y = list(range(20, 0, -3))
print(y)

x = [0] * 5
print(x)
y = 5 * [0, 2]
print(y)

x = list(map(int, input().split()))
print(x)
n, m , *y = x
print(n)
print(m)
print(y)

