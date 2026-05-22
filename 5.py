n = int(input())

# O(n)
mx = 0
arr = []

# ищу самый большой x+y
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
    if x+y>mx:
        mx = x+y

print(mx)

import turtle

sz = 520
turtle.setup(sz, sz)

t = turtle.Turtle()
t.speed(0)

# масштаб
k = (sz-180)//mx
if k<1:
    k = 1

# сдвиг
st = -(mx*k)//2

# сам треугольник
t.up()
t.goto(st, st)
t.down()
t.goto(st+mx*k, st)
t.goto(st, st+mx*k)
t.goto(st, st)

# точки
for p in arr:
    t.up()
    t.goto(st+p[0]*k, st+p[1]*k)
    t.dot(5, "red")

turtle.done()
