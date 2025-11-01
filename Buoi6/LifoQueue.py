from queue import LifoQueue

L = LifoQueue()
for x in [3, 7, "abc", [4,5]]: L.put(x)

print(L.queue)
while L.qsize():
    print(L.get())
    