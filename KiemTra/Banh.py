n = int(input())
a = list(map(int ,input().split()))
tong1 = sum(a)
tong2 = 0
kc = abs(tong1) if n <= 1 else abs(tong1 - 2 * a[0])
for i in a:
	tong2 += i
	kc = min(kc, abs(tong1 - 2 * tong2))
print(kc)
    