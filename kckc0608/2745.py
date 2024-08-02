n, b = input().split()
b = int(b)

pos = 1
ans = 0
for c in reversed(n):
    if c.isnumeric():
        ans += pos * int(c)
    else:
        ans += pos * (ord(c) - ord('A') + 10)

    pos *= b

print(ans)