from queue import LifoQueue
def cs3():
    n = int(input())
    L = LifoQueue()
    while n > 0:
        L.put(n%3)
        n//=3
    print(*L.queue[::-1], sep="")
    # while(not L.empty()): print(L.get(), end= "")
    # print("\n")
if __name__ == "__main__":
    for _ in range(int(input())): cs3()
        
    