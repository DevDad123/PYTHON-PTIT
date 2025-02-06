def prime_fac(n):
    res = ["1"]
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        res.append(f"2^{count}")
    i = 3
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            res.append(f"{i}^{count}")
        i += 2

    if n > 1:
        res.append(f"{n}^1")

    print(" * ".join(res))


t = int(input())
for _ in range(t):
    n = int(input())
    prime_fac(n)