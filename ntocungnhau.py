import math
n,k = map(int, input().split())

start = 10 ** (k - 1)
end = 10 ** k
cnt = 0

for i in range(start, end):
    if math.gcd(i, n) == 1:
        cnt += 1
        print(i,end = " ")
        if cnt % 10 == 0:
            print()