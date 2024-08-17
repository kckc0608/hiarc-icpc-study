from collections import deque
n=int(input())
lst=deque(x for x in range(1,n+1))

while True:
    if len(lst)==1:
        break
    else:
        lst.popleft()
        if len(lst)==1:
            break
        else:
            x=lst.popleft()
            lst.append(x)

print(*lst)