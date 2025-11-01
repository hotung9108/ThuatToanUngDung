from queue import PriorityQueue
Q = PriorityQueue()
A = [[] for i in range(10**5+1)]
n = int(input())
res = 0
for i in range(n):
    t, v = map(int, input().split())
    A[t].append(v)
for i in range(10**5+1, 0, -1):
    for x in A[i]: Q.put(-x)
    if not Q.empty(): res -= Q.get()
print(res)