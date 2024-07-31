apartment = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    apartment[0][i] = i

for floor in range(1, 15):
    for house in range(15):
        apartment[floor][house] = sum(apartment[floor-1][:house+1])

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    assert 1 <= k <= 14
    assert 1 <= n <= 14
    print(apartment[k][n])