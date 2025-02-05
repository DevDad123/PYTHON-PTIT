import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())  
for _ in range(t):
    a, b = map(int, input().split()) 
    gcd = math.gcd(a, b)
    digitsum = 0
    for i in str(gcd):
        digitsum += int(i)
    if is_prime(digitsum):
        print("YES")
    else:
        print("NO")
