t = int(input())
for _ in range(t):
    s = input().strip()
    if len(s) < 2:
        print("NO")
    elif s[:2] == s[-2:]:
        print("YES")
    else:
        print("NO")
