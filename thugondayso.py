n = int(input()) 
a = list(map(int, input().split()))  

stack = []
for i in range(n):
    if stack and (a[stack[-1]] + a[i]) % 2 == 0:
        stack.pop()
    else:
        stack.append(i)
print(len(stack))