n=int(input())

d=len(str(n))
x=max(1,n-d*9)

for i in range(x,n):
    lst=list(str(i))
    s=0
    for j in lst:
        s+=int(j)
    if s+i==n:
        print(i)
        break
else:
    print(0)