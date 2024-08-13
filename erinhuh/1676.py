n=int(input())

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

x=fac(n)
lst=list(str(x))
lst.reverse()

ans=0
while True:
    if lst[ans]!='0':
        print(ans)
        break
    else:
        ans+=1