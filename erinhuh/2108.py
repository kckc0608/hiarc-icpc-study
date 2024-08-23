import sys
input=sys.stdin.readline

n=int(input())
lst=[]
sum=0
for i in range(n):
    a=int(input())
    lst.append(a)
    sum+=a

print(round(sum/n))

lst.sort()
print(lst[(n-1)//2])

lst2=[0]*8001
for i in lst:
    lst2[i+4000]+=1
if lst2.count(max(lst2))==1:
    print(lst2.index(max(lst2))-4000)
else:
    lst2.remove(max(lst2))
    print(lst2.index(max(lst2))-3999)

print(lst[-1]-lst[0])