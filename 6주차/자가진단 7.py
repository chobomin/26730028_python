h, m = map(int, input().split())

if h >= 12:
    if h> 12:
        h=h-12
    a="PM"
else:
    a="AM"


if h < 10:
    print("0", end="")
print(h, end=":")

if m < 10:
    print("0", end="")
print(m, a)
