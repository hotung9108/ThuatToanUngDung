import queue
n, k = map(int, input().split())
Q = queue.Queue()
for i in range(1, n+1): Q.put(i)
while Q.qsize() > 1:
    for i in range(k -1):
        Q.put(Q.get())
        Q.get()
print(Q.get())