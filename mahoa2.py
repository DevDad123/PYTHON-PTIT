p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
encode = ""
k = int(input())
s = str(input())
for char in s:
    newindex = (p.index(char) + k) % 28
    encode += p[newindex]
print(encode[::-1])

