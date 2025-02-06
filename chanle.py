def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum
def diff_two_value(n):
    for i in range(0,n):
        for j in range(i+1,n):
            if abs(n[i] - n[j]) == 2:
                return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    if(sum_of_digits(n) % 10 == 0 and diff_two_value(n)):
        print("YES")
    else:
        print("NO")

