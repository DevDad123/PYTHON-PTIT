t = int(input())
s = str("")
for i in range(t):
    s = str(input())
    res = str("")
    a = []
    for char in s:
        if(char.isdigit()):
            res += char
        else:
            if(res != ""):
                a.append(int(res))
                res = ""
    if(res != ""):
        a.append(int(res))
    a.sort()
    print(a[0])


