from functools import lru_cache

@lru_cache(maxsize=None)

def room(k,n):
    
    if k==0:
        return n
    nop=0    
    for i in range(1,n+1):
        nop+=room(k-1,i)
    return nop
num=int(input())
for x in range(num):
    k=int(input())
    n=int(input())
    print(room(k,n))
        