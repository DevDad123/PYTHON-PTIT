a, K, N = map(int, input().split())

b_list = []
start = ((a // K) + 1) * K - a 

for b in range(start, N - a + 1, K):
    if b > 0:
        b_list.append(str(b))

print(" ".join(b_list) if b_list else -1)
