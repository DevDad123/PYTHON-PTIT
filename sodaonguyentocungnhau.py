import math

def is_so_dao(n,n1):
    if math.gcd(int(n),int(n1)) == 1:
        return True
    return False

t = int(input())
for _ in range(t):
    n = input()
    n1 = n[::-1]
    if is_so_dao(n,n1):
        print("YES")
    else:
        print("NO")

