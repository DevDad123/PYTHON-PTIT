def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total


def diff_two_value(n):
    digits = [int(d) for d in str(n)]

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if abs(digits[i] - digits[j]) == 2:
                return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())

    if sum_of_digits(n) % 10 == 0 and diff_two_value(n):
        print("YES")
    else:
        print("NO")