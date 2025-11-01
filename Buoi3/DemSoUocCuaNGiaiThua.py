def sang(n):
    s = [1]*(1+n)
    for i in range(2, n+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j] = 0
    return s
                            
if __name__ == "__main__":
    s = sang(1000)
    n = int(input())
    res = 1
    for i in range(2, n+1):
        d = 1
        if s[i]:
            m = n
            while m > 0:
                m//=i
                d+=m
        res = res *d %1000000007
    print(res)