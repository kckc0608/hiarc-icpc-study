n = int(input())
s = input()

MOD = 1234567891

answer = 0
for i in range(n):
    now_value = (ord(s[i]) - ord('a')+1)
    for j in range(i):
        now_value *= 31
        now_value %= MOD

    answer += now_value
    answer %= MOD


print(answer)