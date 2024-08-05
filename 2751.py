

n=int(input())
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x)

for item in tuple(sorted(lst)):
    print(item)