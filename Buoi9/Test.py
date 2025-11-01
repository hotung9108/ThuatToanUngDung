from queue import PriorityQueue
# Q = PriorityQueue()
# for x in 243, 53, 61, 73, 44, 756, 84, 52, 73: Q.put(x)

# while Q.qsize():
#     print(Q.get(), end=" ")
    
class duLieu:
    def __init__(self, x): self.elem = x
    def __lt__(self, other):
        if self.elem%3 == other.elem%3: 
            return self.elem <other.elem
        return self.elem%3 < other.elem%3

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    Q = PriorityQueue()
    for x in arr:
        Q.put(duLieu(x))
    result = []
    while Q.qsize():
        result.append(Q.get().elem)
    print(" ".join(map(str, result)))