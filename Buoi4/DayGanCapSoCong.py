# def csc(a):
#     d = a[1] - a[0]
#     return all (d == y - x for x, y in zip(a, a[1:]))
 
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     if csc(a): print("Day cap so cong")
#     elif csc(a[1:]): print("Day gan cap so cong tai 1")
#     elif csc(a[:n-1]): print("Day gan cap so cong tai n")
#     else:
#         for i in range(1, n-1):
#             if(a[i-1]+a[i+1])%2 == 0:
#                 x = (a[i-1] + a[i+1])//2
#                 y = a[i]
#                 a[i] = x
#                 if csc(a):
#                     print("Day gan cap so cong tai %d" %(i+1))
#                     break
#                 a[i] = y
#         else: print("Khong la gan csc")

# from collections import namedtuple
# sv = namedtuple("sinhvien", "ten tuoi diem")
# x = sv("le van hung", 13, 5.2)
# print(x)
# print(x.ten)

from collections import namedtuple
diem = namedtuple("Diem", "x, y")
n = int(input())
A = set()
for i in range(n):
    x, y = map(int, input().split())
    A.add(diem(x, y))
print("NO" if len(A) == n else "YES")