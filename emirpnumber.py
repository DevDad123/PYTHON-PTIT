def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def reverse_number(n):
    return int(str(n)[::-1])

t = int(input())
for _ in range(t):
    n = int(input())
    emirp_numbers = []
    for i in range(2, n):
        if is_prime(i):
            reversed_i = reverse_number(i)
            if is_prime(reversed_i) and i != reversed_i:
                emirp_numbers.append(i)
    print(" ".join(map(str, emirp_numbers)))