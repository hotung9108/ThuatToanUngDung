class ptb2:
    def __init__(self, _a = 0, _b= 0, _c= 0):
        self.a = _a
        self.b = _b
        self.c = _c   
    def nhap(self):
        _a, _b, _c = map(float, input().split())
        self.a = _a
        self.b = _b
        self.c = _c
    def __str__(self):
        return str(self.a) + "x^2" + str(str.b) + "x+" + str(self.c) + "=0"
    def giai(self):
        if self.a==self.b == self.c==0: print("vo so nghiem")
        elif self.a == self.b == 0: print("vo nghiem")
        elif self.a == 0: print("%.3f"%(-self.c/self.b))
        else:
            self.b/=-2*self.a
            self.c/=self.a
            d = self.b**2-self.c
            if d < 0: print("vo nghiem")
            elif d == 0: print("%.3f" %(self.b))
            else:
                d = d**.5
                print("%.3f\n%.3f"%((self.b-d), (self.b+d)))
if __name__ == '__main__':
    p = ptb2()
    p.nhap()
    p.giai()