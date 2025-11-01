from queue import PriorityQueue

if __name__ == "__main__":
    Q = PriorityQueue()
    n = int(input())
    k = 0
    z = 0
    V = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for v, t in zip(V, T):
        Q.put(v + k)
        z = 0
        while Q.qsize() > 0 and Q.queue[0] - k <= t: z += Q.get()-k
        print(z+t*Q.qsize(), end = " ")
        k += t
        if Q.qsize() == 0:
            k = 0
    
