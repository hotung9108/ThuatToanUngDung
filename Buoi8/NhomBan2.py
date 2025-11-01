import queue
A=[[] for i in range(10**5+2)]
d=[0]*(10**5+1)
def Tim(k, Q):  # tra ve so phan tu cua nhom chua k
    global d,A
    Q.put(k)
    dem = 1
    d[k] = 1
    while Q.qsize():
        u = Q.get()
        for v in A[u]:
            if d[v] == 0:
                d[v] = 1
                dem += 1
                Q.put(v)
    return dem
if __name__ == '__main__':
    n, m = map(int, input().split())  
    for i in range(m):
        x, y = map(int, input().split())
        A[x].append(y)
        A[y].append(x)
    res,g = 0,0
    Q=queue.Queue()
    for i in range(1, n + 1):
        if d[i] == 0:
            g += 1
            res = max(res, Tim(i, Q))
    print(g, res, sep="\n")