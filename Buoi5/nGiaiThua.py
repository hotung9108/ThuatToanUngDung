import itertools
n = int(input())
a = list(itertools.accumulate(range(1,n),lambda x, y:x*y))
print((a[-1]))
