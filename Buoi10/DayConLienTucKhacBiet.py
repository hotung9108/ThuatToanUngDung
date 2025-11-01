# if __name__ == "__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     L = 0
#     D = {}
#     res = 0
#     for i, x in enumerate(a, 1):
#         if x in D.keys() and D[x] > L: L = D[x]
#         res = max(res, i - L)
#         D[x] = i
#     print(res)
            
if __name__ == '__main__':
    n = int(input())
    