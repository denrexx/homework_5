s = input()

# O(n)
if s=="{}":
    print(0)
else:
    # убрал скобки
    s = s[1:-1]
    # разбил по запятой
    arr = s.split(", ")
    print(len(set(arr)))
