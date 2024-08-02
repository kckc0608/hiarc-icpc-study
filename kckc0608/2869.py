a, b, v = map(int, input().split())
days = (v - a) // (a-b)
height = days * (a-b)
while True:
    height += a
    days += 1
    if height >= v:
        break

    height -= b
print(days)