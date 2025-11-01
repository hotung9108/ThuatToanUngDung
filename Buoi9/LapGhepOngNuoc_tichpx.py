from queue import PriorityQueue
Q = PriorityQueue()
n, k = map(int, input().split())
for x in map(int, input().split()):
    Q.put(x)
res = 0
while Q.qsize()>1:
    t = 0
    z = min (k, Q.qsize())
    
    for i in range(z): t += Q.get()
    Q.put(t)
    res+=t
print(res)