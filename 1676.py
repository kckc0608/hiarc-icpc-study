#1676


def fact(x):
    if x==0 or x==1:
        return 1
    t=1
    while x>=2:
        t=t*x
        x=x-1
    return t

n=int(input())

for i in range(n):
    l=int(input())
    a=str(fact(l))[-1::]
print(a)
for x in a:
    if x!='0':
        print(x)
        break
    
