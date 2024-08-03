n,k=map(int,input().split())

def fac(a):
    if a==0:
        return 1
    else:
        return a*fac(a-1)
    
print(fac(n)//(fac(k)*fac(n-k)))