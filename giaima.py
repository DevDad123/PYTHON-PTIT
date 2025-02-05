t = int(input())
for _ in range(t):
    s = str(input())
    for i in range(0, len(s) , 2):
        print(s[i]*int(s[i+1]), end = '')
    print('')