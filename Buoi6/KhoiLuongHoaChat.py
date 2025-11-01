def tinh_khoi_luong(x):
    K = {'C': 12, 'O': 16, 'H': 1, '(': 0}
    S = []
    for c in x:
        if c in K:
            S.append(K[c])
        elif c == ')':
            t = 0
            while S and S[-1] != 0:
                t += S.pop()
            if S:  # pop '('
                S.pop()
            S.append(t)
        elif c.isdigit():
            if S:
                S[-1] *= int(c)
    return sum(S)

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        x = input().strip()
        print(tinh_khoi_luong(x))