from queue import PriorityQueue


if __name__ == "__main__":
    n, k = map(int, input().split())
    doan_ong = list(map(int,input().split()))
    Q = PriorityQueue()
    kq = 0
    for ong in doan_ong:
        Q.put(ong);
    while Q.qsize() > 1:
        temp = 0
        for _ in range(min(k, Q.qsize())):
            temp += Q.get()
        kq += temp
        Q.put(temp)
    print(kq)
        