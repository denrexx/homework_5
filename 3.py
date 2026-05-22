n = int(input())
arr = list(map(int, input().split()))

# O(n+m)
d = {}
# сумма для каждого числа
for x in arr:
    if x in d:
        d[x] += x
    else:
        d[x] = x

if len(d)==0:
    print(0)
else:
    m = max(d)
    dp = [0] * (m+1)
    dp[1] = d.get(1, 0)

    # либо берем i, либо нет
    for i in range(2, m+1):
        dp[i] = max(dp[i-1], dp[i-2] + d.get(i, 0))

    print(dp[m])
