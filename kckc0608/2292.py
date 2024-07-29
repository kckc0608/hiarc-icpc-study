count = 1
v = 1
n = int(input())
a = 0
while v < n:
    a += 6
    v += a
    count += 1

print(count)