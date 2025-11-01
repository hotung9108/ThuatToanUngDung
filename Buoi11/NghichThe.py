class node:
    def __init__(self, u, v):
        self.A, self.B, self.elem = u, v , 0
        if u + 1 == v: self.left, self.right = None, None
        else:
            self.left = node(u,(u+v)//2)
            self.right = node((u+v)//2, v)
res = 0
def add(T, x):
    global res 
    T.elem += 1
    if T.left != None:
        if x < T.left.B:
            res += T.right.elem
            add(T.left, x)
        else:
            add(T.right, x)
if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    T = node(1, n+1)
    for x in a: add(T, x)
    print(res)