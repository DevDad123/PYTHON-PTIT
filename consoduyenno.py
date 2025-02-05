t = int(input())
for _ in range(t):
    s = str(input())
    if s[0] == s[len(s) - 1]:
        print("YES")
    else:
        print("NO")