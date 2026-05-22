s = input()

if s=="{}":
    print(0)
else:
    s = s[1:-1]
    arr = s.split(", ")
    print(len(set(arr)))
