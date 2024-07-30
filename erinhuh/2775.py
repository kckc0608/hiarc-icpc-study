t=int(input())

ans=[]
for i in range(t):
    k=int(input())
    n=int(input())
    lst=list(m+1 for m in range(n))
    for j in range(k):
        for l in range(n):
            if l==0:
                continue
            else:
                lst[l]+=lst[l-1]
    ans.append(lst[-1])

for i in ans:
    print(i)