n = int(input())

mx = 0
arr = []

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

k = (sz-180)//mx
if k<1:
    k = 1

st = -(mx*k)//2

t.up()
t.goto(st, st)
t.down()
t.goto(st+mx*k, st)
t.goto(st, st+mx*k)
t.goto(st, st)

for p in arr:
    t.up()
    t.goto(st+p[0]*k, st+p[1]*k)
    t.dot(5, "red")

turtle.done()