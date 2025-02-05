def round_to_nearest_10(n):
    return (n // 10 + 1) * 10 if n % 10 >= 5 else (n // 10) * 10

t = int(input())  
for _ in range(t):  
    n = int(input())  
    print(round_to_nearest_10(n))
