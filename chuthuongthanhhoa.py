
s = str(input())
cntlower = 0
cntupper = 0
for i in range(len(s)):
    if s[i].isupper():
        cntupper += 1
    else:
        cntlower += 1
if cntlower >= cntupper:
    print(s.lower())
else:
    print(s.upper())
    
        