# Bien luan phuong trinh bac 2
a, b, c = map(float, input().split)
b/=-2 
d = b*b - a * c
if a==b==c==0: print("vo so nghiem")
elif a==b==0 or d < 0: print("vo nghiem")
elif a==0: print("%.3f", c/2/b)
elif d == 0: print("%.3f", b/a)
else :
    d = d**0.5
    x1 = (b-d)/a
    x2 = (b+d)/a
    if x1 > x2 : x1, x2 = x2, x1
    print("%.3f\n %.3f", x1, x2)