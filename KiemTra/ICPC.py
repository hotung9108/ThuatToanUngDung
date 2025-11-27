t = int(input())
test = []
for i in range(t):
    s = set()
    n = int(input())
    str = ''
    kq = 0
    str = input()
    for j in str:
        if j in s:
            kq += 1
        else:
            kq += 2
            s.add(j)
    print(kq)
        
            
            
        
    