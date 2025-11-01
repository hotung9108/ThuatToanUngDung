def Fibo(n):
    if n==0: return 1, 0
    x, y = Fibo(n//2)
    x, y = (x*x + y *y)%1000000009, (x*y+y*(x-y))%1000000009
    if n%2==0: return x%1000000009, y%1000000009
    return (x+y)%1000000009 , x%1000000009

if __name__ == '__main__':
    # for i in range(100):+
    #     a, b = Fibo(i)
    #     print(a, end = " ")
    # a, b = Fibo(5)
    # # print(a)     
    # x = input()
    # y = int(input())
    # z = float(input())
    # print(x, y, z)
    
    # u, v = input().split()
    # u = int(u)
    # v = int(v)
    # print(u + v)
    
    x , y , z = input("Nhap ngay").split("\\")
    x, y, z = int(x), int(y), int(z)
    print("ngày %d tháng %d năm %d" %(x, y, z))