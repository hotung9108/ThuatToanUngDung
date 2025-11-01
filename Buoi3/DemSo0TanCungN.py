class Solve:
    def baitap(n):
        d = 0
        for i in range(5, n+1, 5):
            while (i % 5 == 0):
                i  //=5
                d += 1
        print(d)     
    def baitap2(n):
        d = 0
        while(n > 0):
            n//=5
            d+=n
        print(d)

if __name__ == "__main__":
    n = int(input("Nhap n:"));
    Solve.baitap2(n)
    