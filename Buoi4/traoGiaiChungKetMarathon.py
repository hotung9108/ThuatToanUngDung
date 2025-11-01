# x = "Duong Viet Duc ANh 628 DDT"
# a, b, c = x.rsplit('', maxsplit=2)
# b = int(b)
# print(a)
# print(b)
# print(c)

from collections import namedtuple
sv = namedtuple("sv", "ten diem")

if __name__ == '__main__':
    n = int(input())
    D = []
    K = []
    for i in range(n):
        ten, diem, khoa = input().rsplit('', 2)
        if khoa == "DDT": D.append(sv(ten, int(diem)))
        else: K.append(sv) 