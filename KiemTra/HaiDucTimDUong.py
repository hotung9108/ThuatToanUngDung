from collections import deque
chia = 10**9 + 7
n,m = map(int,input().split())
d = [[] for _ in range(n + 1)]
k = [0] * (n + 1)
for _ in range(m):
    x,y = map(int,input().split())
    d[x].append(y)
    k[y] += 1
dp = [0] * (n + 1)
dp[1] = 1
q = deque()
for i in range(1, n + 1):
    if k[i] == 0:
        q.append(i)
while q:
    u = q.popleft()
    for v in d[u]:
        dp[v] = (dp[v] + dp[u]) % chia
        k[v] -= 1
        if k[v] == 0:
            q.append(v)
print(dp[n] % chia)