import math
def sum_of_fac(s):
    sum = 0
    for i in range(len(s)):
        sum += math.factorial(int(s[i]))
    if sum == int(s):
        return True
    return False

t = int(input())
for _ in range(t):
    s = str(input())
    if sum_of_fac(s):
        print("Yes")
    else:
        print("No")
