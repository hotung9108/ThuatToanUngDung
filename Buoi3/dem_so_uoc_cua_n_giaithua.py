class Solution:
    def eratos(n):
        s=[1]*(1+n)
        for i in range(2,n+1):
            if s[i]:
                for j in range(i*i, n+1, i): 
                    s[j] = 0
        return s
    def solve(s,n):
        res = 1
        for i in range(2, n+1):
            d=1
            if s[i]:
                m=n
                while m>0:
                    m //= i
                    d += m

            res = res*d%1000000007
        return res
    
if __name__ == "__main__":
    n = int(input())
    sieved = Solution.eratos(n)
    res = Solution.solve(sieved,n) 
    print(res)
