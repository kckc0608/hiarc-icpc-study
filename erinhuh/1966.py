n=int(input())

ans=[]
for i in range(n):
    a,b=map(int,input().split())
    lst=list(map(int,input().split()))
    s=0
    while True:
        if lst[b]!=max(lst):
            if max(lst)==lst[0]:
                lst.remove(max(lst))
                b-=1
                s+=1
            else:
                f=lst[0]
                lst.remove(f)
                lst.append(f)
                if b!=0:
                    b-=1
                else:
                    b=len(lst)-1
        elif lst[b]==max(lst):
            if b==0:
                s+=1
                break
            else:
                if lst[0]==max(lst):
                    lst.remove(lst[0])
                    s+=1
                    b-=1
                else:
                    f=lst[0]
                    lst.remove(f)
                    lst.append(f)
                    b-=1
    ans.append(s)

for i in ans:
    print(i)