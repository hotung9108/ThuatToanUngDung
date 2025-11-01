if __name__ == '__main__':
    D = {0: 0}
    a = input()
    s = 0
    res = 0
    for i, x in enumerate(a, 1):
        s += -1 if x == 'X' else 1
        L = D.get(s, i)
        res = max(res, i-L)
        if s not in D.keys(): D[s] = i
    print(res)