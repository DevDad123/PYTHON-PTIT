def check_distance(s1):
    s2 = s1[::-1]
    for i in range(1,len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            return False
    return True

t = int(input())
for _ in range(t):
    s1 = str(input())
    if check_distance(s1):
        print("YES")
    else:
        print("NO")
