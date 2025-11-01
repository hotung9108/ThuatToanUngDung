class node:
    def __init__(self,u,v):
        self.A,self.B,self.elem=u,v,-1e9
        if u+1==v:
            self.left = None
            self.right = None 
        else:
            self.left = node(u,(u+v)//2)
            self.right = node((u+v)//2,v)

def add(T,p,x):
    T.elem = max(T.elem,x)
    if T.left != None:
        if p<T.left.B: add(T.left,p,x)
        else: add(T.right,p,x)

def get(T,L,R):
    if T.A == L and T.B == R: return T.elem
    if R<=T.left.B: return get(T.left,L,R)
    if L>=T.right.A: return get(T.right,L,R)
    return max(get(T.left,L,T.left.B),get(T.right,T.right.A,R))

if __name__ == "__main__":
    n,m=map(int,input().split())
    a = list(map(int,input().split()))
    T = node (1,n+1)

    for i,x in enumerate(a,1): add(T,i,x)
    for i in range(m):
        L,R = map(int,input().split())
        print(get(T,L,R+1))    