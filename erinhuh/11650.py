n=int(input())

lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x: (x[0], x[1]))

for i in lst:
    print(*i)