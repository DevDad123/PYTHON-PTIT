def round_number(n):
    place = 10
    while place <= n:
        if n % place >= place // 2:
            n = (n // place + 1) * place
        else:
            n = (n // place) * place
        place *= 10
    return n

t = int(input())

for _ in range(t):
    n = int(input())
    print(round_number(n))
