D = {4: 'a', 'b': [1,2], (3,4) : "abc"}
# print(D[4])
for x in D.keys(): print(x, "->", D[x])

#
# D[0] = "Khong co"

# for y in D.values(): print(y, end=" ")

# print("\nItems: ")
# for x, y in D.items(): print(x, "->" ,y)

# khong chac co thi dung get

print(D.get(10, "lam gi co 10 trong tu dien"))

D.pop()



