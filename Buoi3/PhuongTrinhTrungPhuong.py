def dem(t):
    if t < 0: return 0
    if t == 0: return 1
    return 2
if __name__ == '__main__':
    a, b, c = map(float, input().split())
    b /= 2
    d = b*b - a*c
    if a==b==c==0: print(-1)
    elif a==b==0 or d < 0: print(0)
    elif a==0: print(dem(-c/2/b))
    elif d==0: print(dem(-b/a))
    else:
        x1 = (-b-d**.5)/a
        x2 = (-b+d**.5)/a
        print(dem(x1) + dem(x2))