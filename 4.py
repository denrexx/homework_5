t = int(input())

# O(t*n)
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    # минимумы
    ma = min(a)
    mb = min(b)

    s = 0
    for i in range(n):
        x = a[i] - ma
        y = b[i] - mb
        # тут считаю ходы отдельно
        s += x+y

    print(s)
