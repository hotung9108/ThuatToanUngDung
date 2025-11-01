def sol():
    m, n, k = map(int ,input().split())
    res = m // n
    nap = res
    while nap >= k:
        res += nap // k
        nap = nap // k + nap%k
    print(res)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t): sol()