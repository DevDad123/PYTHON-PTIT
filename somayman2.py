def is_lucky(n):
    for digit in n:
        if digit != '4' and digit != '7':
            return False
    return True

t = int(input())
for _ in range(t):
    n = input().strip()
    if is_lucky(n):
        print("YES")
    else:
        print("NO")