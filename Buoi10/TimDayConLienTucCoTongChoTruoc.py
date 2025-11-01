if __name__ == '__main__':
    D = {0:0}
    n , T = map(int, input().split())
    res = 0
    s = 0
    a = list(map(int, input().split()))
    for i, x in enumerate(a, 1):
        s = s + x
        L = D.get(s-T, i)
        res = max(res, i - L)
        if s not in D.keys():
            D[s] = i
    print(res)