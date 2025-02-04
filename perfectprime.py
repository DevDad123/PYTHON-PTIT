import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_num(n):
    return int(str(n)[::-1])

def check_digit_prime(n):
    for digit in str(n):
        if digit not in '2357':  
            return False
    return True

def sum_of_digit(n):
    return sum(int(digit) for digit in str(n))

def check_perfect_prime(n):
    if not is_prime(n):
        return False
    reversed_n = reverse_num(n)
    if not is_prime(reversed_n):
        return False
    if not is_prime(sum_of_digit(n)):
        return False
    if not check_digit_prime(n):
        return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    if check_perfect_prime(N):
        print("Yes")
    else:
        print("No")
