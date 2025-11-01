from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    V = list(map(int, input().split()))
    T = list(map(int, input().split()))
    Q = PriorityQueue()
    t = 0
    for i in range(n):
        Q.put(V[i] + t)
        Z = 0
        while not Q.empty() and Q.queue[0] - t <= T[i]:
            Z += Q.get() - t
        print(Z + Q.qsize() * T[i], end=" ")
        t += T[i]
        if Q.qsize() == 0:
            t = 0