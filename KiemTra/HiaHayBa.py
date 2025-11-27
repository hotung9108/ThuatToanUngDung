if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    while len(arr) < n:
        arr += list(map(int, input().strip().split()))
    if n == 1:
        print(arr[0])
    elif n == 2:
        print(arr[0] * arr[1])
    else:
        arr.sort()
        max1, max2 = arr[-1], arr[-2]
        max3 = arr[-3]
        min1, min2 = arr[0], arr[1]
        kq = [
            max1 * max2,           
            min1 * min2,          
            max1 * max2 * max3,    
            min1 * min2 * max1     
        ]
        print(max(kq))