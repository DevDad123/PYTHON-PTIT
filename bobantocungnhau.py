import math
def nto_cung_nhau(n1,n2):
    if math.gcd(n1,n2) == 1:
        return True
    return False

l,r = map(int,input().split())
for i in range(l,r-1):
    for j in range(i+1,r):
        for k in range(j+1,r+1):
            if nto_cung_nhau(i,j) and nto_cung_nhau(j,k) and nto_cung_nhau(i,k):
                print(f"({i}, {j}, {k})")