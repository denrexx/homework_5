n = int(input())
arr = list(map(int, input().split()))

c1 = 0
c2 = 0
c3 = 0
c4 = 0

for x in arr:
    if x==1:
        c1 += 1
    elif x==2:
        c2 += 1
    elif x==3:
        c3 += 1
    else:
        c4 += 1

res = c4

mn = min(c1, c3)
res += mn
c1 -= mn
c3 -= mn

res += c2//2
if c2%2==1:
    res += 1
    c1 -= 2

if c1>0:
    res += (c1+3)//4

if c3>0:
    res += c3

print(res)
