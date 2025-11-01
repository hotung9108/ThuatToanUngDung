import math


class ps:
    def __init__(self, _t = 0, _m = 1): self.t, self.m = _t, _m
    def __add__(self, other):
        return ps(self.t*other.m + self.m * other.t, self.m*other.m)
    def __str__(self): return str(self.t) + "/" + str(self.m)
    def rg(self):
        d = abs(math.gcd(self.t, self.m))
        if self.m < 0: d = -d
        self.t//=d
        self.m//=d
    def nghichdao(self):
        return ps(self.m, self.t)
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    p = ps(a[0], 1)
    for x in a[1:]:
        q = p.nghichdao()
        p = ps(x, 1) + q
    print(p)
        