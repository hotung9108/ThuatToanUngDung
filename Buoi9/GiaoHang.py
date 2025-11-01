from queue import PriorityQueue

def giao_hang(n, data):
    A = [[] for i in range(10**6 + 1)]
    for t, v in data:
        A[t].append(v)
    res = 0
    Q = PriorityQueue() 
    for i in range(10**6, 0, -1):
        for value in A[i]:
            Q.put(-value)  
        if not Q.empty():
            res += -Q.get() 
    return res
n = int(input())
data = []
for i in range(n):
    t, v = map(int, input().split())
    data.append((t, v))
print("Kết quả:", giao_hang(n, data))