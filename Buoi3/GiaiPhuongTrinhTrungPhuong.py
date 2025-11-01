def dem(t):
    if t < 0: return []
    if t == 0: return [0]
    return [-t**.5, t**.5]

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    b /= 2
    d = b*b - a*c
    if a==b==c==0: print("vo so nghiem")
    elif a==b==0 or d<0: print("vo nghiem")
    else:
        if a==0: res=dem(-c/2/b)
        elif d==0:res=dem(-b/a)
        else: res = dem((-b-d**.5)/a)+ dem((-b+d**.5)/a)
        if res == []: print("vo nghiem")
        else: 
            for x in res : print("%.3f"%x)