n, k = map(int, input().split())
tich = 1
for i in range(k if n%k == 0 else n%k, n+1, k):
    tich *= i
print(tich)