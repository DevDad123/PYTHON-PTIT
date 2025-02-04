t = int(input())
cnt = 1
for _ in range(t):
    s = str(input())
    for i in range(1,len(s)):
        if s[i - 1] != s[i]:
            print(cnt,end = '')
            print(s[i - 1],end = '')
            cnt = 1
        else:
            cnt += 1
    print(cnt,end = '')
    print(s[len(s) - 1], end = '')
