from queue import PriorityQueue
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [[] for i in range(10**6 + 1)]
max_day = max(a) if a else 0
for i in range(n):
    A[a[i]].append(b[i])
Q = PriorityQueue()
res = 0
sum_b = sum(b)
for day in range(max_day, 0, -1):
    for val in A[day]:
        Q.put(-val)
    if not Q.empty():
        res += -Q.get()
print(sum_b - res)