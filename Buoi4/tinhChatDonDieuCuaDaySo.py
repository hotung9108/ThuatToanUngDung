def fun(a, f):
    return all(f(x, y) for x, y in zip(a, a[1:]))

# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     if fun(a, lambda x,y: x < y): print("Day don dieu tang ngat")
#     elif fun(a, lambda x,y: x > y): print("Day don dieu giam ngat")
#     elif fun(a, lambda x, y: x == y): print("Day bang nhau")
#     elif fun(a, lambda x,y:x >= y): print("Day don dieu giam")
#     elif fun(a, lambda x, y: x <= y): print("Day don dieu tang")
#     else: print("Day khong don dieu")

def dem(a, f):
    return any(f(x, y) for x, y in zip(a, a[1:]))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    t = dem(a, lambda x,y: x < y)
    g = dem(a, lambda x,y:x>y)
    b = dem(a, lambda x,y:x==y)
    s=t*4+g*2+b
    kl=["day it hon 2 phan tu", "bang nhau", "giam ngat", "giam", "tang ngat", "tang", "khong dd", "khong dd"]
    print(kl[s])